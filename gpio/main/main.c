#include "driver/gpio.h"
#include <math.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define GPIO_LED GPIO_NUM_2

void print_gpio_config()
{
    uint64_t all_pin_mask = pow(2, 24) - 1;
    gpio_dump_io_configuration(stdout, all_pin_mask);
}

void normal_blink()
{
    gpio_set_direction(GPIO_LED, GPIO_MODE_OUTPUT);
    while(1)
    {
        gpio_set_level(GPIO_LED, 1);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        gpio_set_level(GPIO_LED, 0);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

void read_blink()
{
    gpio_set_direction(GPIO_LED, GPIO_MODE_INPUT_OUTPUT);
    while(1)
    {
        
        gpio_set_level(GPIO_LED, 1);
        printf("Read level: %d\n", gpio_get_level(GPIO_LED));
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        gpio_set_level(GPIO_LED, 0);
        printf("Read level: %d\n", gpio_get_level(GPIO_LED));
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        
    }
}

void app_main()
{
    print_gpio_config();
    read_blink();
}