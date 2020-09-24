module Main exposing (main)

import Html exposing (..)
import Html.Attributes exposing (class, href, id)


view =
    article []
        [ h1 [ class "title" ] [ text "Hello world!" ]
        , h2 [ class "subtitle" ] [ text "Lorem ipsum dolor sit amet" ]
        , p [ class "content" ] [ text "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ]
        ]


main =
    view
