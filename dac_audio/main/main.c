#include "esp_log.h"
#include "hal/dac_types.h"
#include "driver/dac_continuous.h"

#include "bells.h"

void app_main(void)
{
    dac_continuous_config_t dac_continuous_config = 
    {
        .chan_mask = DAC_CHANNEL_MASK_CH0,
        .desc_num = 6,
        .buf_size = 1024,
        .freq_hz = 44100,
        .offset = 0,
        .clk_src = DAC_DIGI_CLK_SRC_APLL
    };
    dac_continuous_handle_t dac_continuous_handle;
    ESP_ERROR_CHECK(dac_continuous_new_channels(&dac_continuous_config, &dac_continuous_handle));
    ESP_ERROR_CHECK(dac_continuous_enable(dac_continuous_handle));
    ESP_ERROR_CHECK(dac_continuous_write(dac_continuous_handle, audio_table, sizeof(audio_table), NULL, -1));
    ESP_ERROR_CHECK(dac_continuous_disable(dac_continuous_handle));
    ESP_ERROR_CHECK(dac_continuous_del_channels(dac_continuous_handle));
}
