// Copyright 2026 Leroy Lu
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum custom_keycodes {
    MODE_AM = SAFE_RANGE,
    MODE_FM,
    NEW_STATION,
    TUNE_DOWN,
    TUNE_UP
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        MODE_AM,       // SW2
        MODE_FM,       // SW3
        NEW_STATION    // Encoder press
    )
};

#if defined(ENCODER_MAP_ENABLE)

const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = {
        ENCODER_CCW_CW(TUNE_DOWN, TUNE_UP)
    }
};

#endif

typedef enum {
    BAND_AM,
    BAND_FM
} radio_band_t;

static radio_band_t current_band = BAND_FM;

// Positions run from 0 to 127 across the OLED.
static uint8_t tuning_position = 64;
static uint8_t target_position = 96;

// Used to generate a different target for each new round.
static uint32_t random_state = 0x6D2B79F5u;

static uint8_t generate_target(void) {
    // Human timing makes the next target less predictable.
    random_state ^= timer_read32();
    random_state ^= ((uint32_t)tuning_position << 16);

    // Xorshift pseudorandom generator.
    random_state ^= random_state << 13;
    random_state ^= random_state >> 17;
    random_state ^= random_state << 5;

    // Keep the target slightly away from the screen edges.
    return 8 + (random_state % 112);
}

static void start_new_round(void) {
    tuning_position = 64;
    target_position = generate_target();
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case MODE_AM:
            if (record->event.pressed) {
                current_band = BAND_AM;
            }
            return false;

        case MODE_FM:
            if (record->event.pressed) {
                current_band = BAND_FM;
            }
            return false;

        case NEW_STATION:
            if (record->event.pressed) {
                start_new_round();
            }
            return false;

        case TUNE_DOWN:
            if (record->event.pressed && tuning_position > 0) {
                tuning_position--;
            }
            return false;

        case TUNE_UP:
            if (record->event.pressed && tuning_position < 127) {
                tuning_position++;
            }
            return false;

        default:
            return true;
    }
}

#ifdef OLED_ENABLE

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_0;
}

static void draw_tuning_slider(void) {
    // Thin horizontal track across the bottom of the 128x32 OLED.
    for (uint8_t x = 0; x < 128; x++) {
        oled_write_pixel(x, 29, true);
    }

    // Three-pixel-wide tuning marker.
    for (uint8_t y = 26; y < 32; y++) {
        oled_write_pixel(tuning_position, y, true);

        if (tuning_position > 0) {
            oled_write_pixel(tuning_position - 1, y, true);
        }

        if (tuning_position < 127) {
            oled_write_pixel(tuning_position + 1, y, true);
        }
    }
}
static uint8_t make_noise(uint8_t x, uint8_t frame) {
    uint16_t value = (uint16_t)x * 37u;
    value += (uint16_t)frame * 17u;
    value += (uint16_t)target_position * 13u;

    value ^= value << 5;
    value ^= value >> 3;

    return (uint8_t)value;
}

static void draw_waveform(void) {
    uint8_t distance;

    if (tuning_position > target_position) {
        distance = tuning_position - target_position;
    } else {
        distance = target_position - tuning_position;
    }

    // Far from the station = noisy waveform.
    // Close to the station = nearly flat waveform.
    uint8_t amplitude = distance / 5;

    if (amplitude > 10) {
        amplitude = 10;
    }

    uint8_t frame = (uint8_t)(timer_read32() >> 6);
    uint8_t previous_y = 13;

    for (uint8_t x = 0; x < 128; x++) {
        int8_t offset = 0;

        if (amplitude > 0) {
            uint8_t range = (amplitude * 2) + 1;
            offset = (int8_t)(make_noise(x, frame) % range) - amplitude;
        }

        uint8_t y = 13 + offset;

        // Connect each point to the previous point.
        uint8_t top = previous_y < y ? previous_y : y;
        uint8_t bottom = previous_y > y ? previous_y : y;

        for (uint8_t line_y = top; line_y <= bottom; line_y++) {
            oled_write_pixel(x, line_y, true);
        }

        previous_y = y;
    }
}

bool oled_task_user(void) {
    oled_clear();

    draw_waveform();
    draw_tuning_slider();

    return false;
}

#endif