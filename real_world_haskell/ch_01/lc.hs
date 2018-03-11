-- lines beginning with "--" are comments.
-- calculate number of lines in text input

main = interact wordCount
    where wordCount input = show (length (lines input)) ++ "\n"
