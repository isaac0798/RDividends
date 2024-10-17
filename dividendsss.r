data <- read.csv("orders.csv")

dividends <- data[data$Action == "Dividend (Dividend)", ]

sum(dividends$Total)
