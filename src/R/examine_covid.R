library(tidyverse)

df <- read_csv('~/Courses/data_wrangling/data/R_lecture/daily-new-confirmed-covid-19-cases-per-million-people.csv')

names(df)

names(df)[3] <- 'new_cases'

df %>%
  filter(Entity %in% c("United States", "Canada", "Brazil")) %>%
  filter(Day >= as.Date("2021-01-01") & Day <= as.Date("2021-03-01")) %>%
  group_by(Entity, Day) %>%
  summarise(new_cases = sum(new_cases, na.rm = TRUE)) %>%
  ggplot(aes(x = Day, y = new_cases, color = Entity)) +
  geom_line() +
  labs(title = "Daily New COVID-19 Cases")


# Using facets and making it a bit prettier
df %>%
  filter(Entity %in% c("United States", "Canada", "Brazil")) %>%
  filter(Day >= as.Date("2021-01-01") & Day <= as.Date("2021-03-01")) %>%
  group_by(Entity, Day) %>%
  summarise(new_cases = sum(new_cases, na.rm = TRUE)) %>%
  ggplot(aes(x = Day, y = new_cases)) +
  geom_line(color = "steelblue") +
  facet_wrap(~ Entity, ncol = 1, scales = "free_y") +
  labs(
    title = "Daily COVID-19 Cases by Country",
    x = NULL,  # cleaner x-axis
    y = "New Cases",
    caption = "Data Source: Our World in Data"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    strip.text = element_text(face = "bold", size = 12),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

#What if we want the US on top?
df %>%
  filter(Entity %in% c("United States", "Canada", "Brazil")) %>%
  mutate(Entity = factor(Entity, levels = c("United States", "Canada", "Brazil"))) %>% # <- Here is the change
  filter(Day >= as.Date("2021-01-01") & Day <= as.Date("2021-03-01")) %>%
  group_by(Entity, Day) %>%
  summarise(new_cases = sum(new_cases, na.rm = TRUE)) %>%
  ggplot(aes(x = Day, y = new_cases)) +
  geom_line(color = "steelblue") +
  facet_wrap(~ Entity, ncol = 1, scales = "free_y") +
  labs(
    title = "Daily COVID-19 Cases by Country",
    x = NULL,  # cleaner x-axis
    y = "New Cases",
    caption = "Data Source: Our World in Data"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    strip.text = element_text(face = "bold", size = 12),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )
