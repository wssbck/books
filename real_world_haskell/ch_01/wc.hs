-- lines beginning with "--" are comments.
-- calculate number of words in text input

main = interact wordCount
    where wordCount input = show (length (words input)) ++ "\n"
