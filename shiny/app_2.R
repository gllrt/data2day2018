ui <- fluidPage(
  titlePanel("Twitter Showcase"),

  # Create a new Row in the UI for Inputs
  fluidRow(
    column(4,
      dateRangeInput(
        "daterange1", 
        "Datumsbereich:",
        start = "2017-01-01",
        end   = Sys.Date(),
        language = "de",
        format = "dd.mm.yyyy",
        separator = " - "
      )
    ),
    column(4,
      textInput("tweetHash", "Hash-Tag oder Benutzer:", "@data2day")
    ),
    column(4,
      sliderInput(
        "NrTweet", 
        "Anzahl von Tweets:", 
        100, 
        2000, 
        500, 
        step = 100, 
        round = TRUE,
        animate = TRUE, 
        width = NULL, 
        sep = ".", 
        dragRange = TRUE
      )
    )
  ),
  # Create a new row for examplary output
  fluidRow(
   column(4,
        verbatimTextOutput("text_daterange1")
    ),
    column(4,
        verbatimTextOutput("text_tweetHash")
    ),
    column(4,
        verbatimTextOutput("text_NrTweet")
    )
  )
)

server <- function(input, output, session) {

  # Render text of date range slider
  output$text_daterange1 <- renderText({
    paste(as.character(input$daterange1, format = "%d.%m.%Y"), collapse = " bis ")
  })

  # Render input from text field
  output$text_tweetHash <- renderText({
    as.character(input$tweetHash)
  })

  # Render interger value from slider
  output$text_NrTweet <- renderText({
    input$NrTweet
  })
  
}

shinyApp(ui = ui, server = server)