library(tidyverse)
library(lubridate)


data <- read_csv("~/reddit_subset_2008.csv")

#firstyear = 1869
#lastyear = 1874

#data <- data %>%
#  filter(year(speechdate) > firstyear) %>%
#  filter(year(speechdate) < lastyear)

data <- data %>%
  select(body, subreddit)

data$body <- data$body %>%
  tolower()

#data <- data %>%
#  filter(str_detect(body, "\\bhe |\\bshe "))

data <- data %>%
  filter(str_detect(body, "\\bman |\\bwoman "))

dir <- setwd("~/")

#write_csv(data, file.path(dir, "reddit_2008_he_she.csv"))

write_csv(data, file.path(dir, "reddit_2008_man_woman.csv"))
