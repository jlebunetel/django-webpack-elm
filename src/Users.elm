module Users exposing (main)

import Browser
import Html exposing (Html, button, div, fieldset, form, h1, h2, hr, i, input, label, option, p, select, span, table, tbody, text, th, thead, tr)
import Html.Attributes exposing (checked, class, classList, disabled, id, name, placeholder, selected, style, type_, value)
import Html.Events exposing (..)
import Http
import Json.Decode as JD exposing (Decoder, field, int, list, map2, map3, map4, string)
import Url.Builder as UB exposing (QueryParameter, crossOrigin, string)


main : Program () Model Msg
main =
    Browser.element
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }


type Msg
    = InputChanged String
      --| LimitChanged (Result String Int)
    | LimitChanged String
    | IsStaffChanged String
    | OrderingChanged String
    | FormSubmitted
    | ResponseReceived (Result Http.Error UsersList)
    | ClearFilters


type alias Option =
    { value : String
    , text : String
    }


orderingModel =
    [ { value = "", text = "Ordering" }
    , { value = "username", text = "Username ↑" }
    , { value = "-username", text = "Username ↓" }
    , { value = "first_name", text = "First Name ↑" }
    , { value = "-first_name", text = "First Name ↓" }
    , { value = "last_name", text = "Last Name ↑" }
    , { value = "-last_name", text = "Last Name ↓" }
    ]


limitModel =
    [ { value = "", text = "Show" }
    , { value = "5", text = "5" }
    , { value = "10", text = "10" }
    ]


type alias User =
    { username : String
    , first_name : String
    , last_name : String
    , is_staff : Bool
    }


type alias UsersList =
    { total : Int
    , results : List User
    }


type alias Model =
    { ordering : String
    , limit : String
    , searchTerms : String
    , usersList : UsersList
    , message : String
    , isStaff : String
    , loading : Bool
    }


initialModel =
    { ordering = ""
    , limit = ""
    , searchTerms = ""
    , usersList =
        { total = 0
        , results =
            []
        }
    , message = ""
    , isStaff = ""
    , loading = False
    }


init : () -> ( Model, Cmd Msg )
init _ =
    update FormSubmitted initialModel


view : Model -> Html Msg
view model =
    div [ id "users" ]
        [ h1 [ class "title" ] [ text "Users list" ]
        , h2 [ class "title is-4" ] [ text "Filters" ]
        , viewForm model
        , hr [] []
        , if model.message == "" then
            h2 [ class "title is-4" ] [ text "Results (", text <| String.fromInt model.usersList.total, text ")" ]

          else
            h2 [ class "title is-4" ] [ text "Error" ]
        , if model.message == "" then
            viewResults model

          else
            viewError model
        ]


viewForm : Model -> Html Msg
viewForm model =
    form
        [ onSubmit FormSubmitted
        ]
        [ fieldset []
            [ div [ class "field is-grouped" ]
                [ div [ class "control has-icons-left" ]
                    [ input
                        [ type_ "text"
                        , classList
                            [ ( "input", True )
                            , ( "is-primary", model.searchTerms /= "" )
                            ]
                        , placeholder "Search"
                        , onInput InputChanged
                        , value model.searchTerms
                        ]
                        []
                    , span [ class "icon is-small is-left" ]
                        [ i [ class "fas fa-search" ] []
                        ]
                    ]
                , viewSelect OrderingChanged model.ordering orderingModel "fas fa-sort"
                , viewSelect LimitChanged model.limit limitModel "fas fa-filter"
                , div [ class "control" ]
                    [ button
                        [ classList [ ( "button is-primary", True ), ( "is-loading", model.loading ) ]
                        , disabled (model.searchTerms == "" && model.ordering == "" && model.limit == "" && model.isStaff == "")
                        , onClick ClearFilters
                        ]
                        [ text "Clear" ]
                    ]
                ]
            , div [ class "field is-grouped" ]
                [ label [ class "label mr-1" ] [ text "Is Staff?" ]
                , div [ class "control" ]
                    [ label [ class "radio" ]
                        [ input
                            [ type_ "radio"
                            , name "is_staff"
                            , value ""
                            , checked (model.isStaff == "")
                            , onInput IsStaffChanged
                            ]
                            []
                        , span [ class "ml-1" ] [ text "All" ]
                        ]
                    , label [ class "radio" ]
                        [ input
                            [ type_ "radio"
                            , name "is_staff"
                            , value "true"
                            , checked (model.isStaff == "true")
                            , onInput IsStaffChanged
                            ]
                            []
                        , span [ class "ml-1" ] [ text "Yes" ]
                        ]
                    , label [ class "radio" ]
                        [ input
                            [ type_ "radio"
                            , name "is_staff"
                            , value "false"
                            , checked (model.isStaff == "false")
                            , onInput IsStaffChanged
                            ]
                            []
                        , span [ class "ml-1" ] [ text "No" ]
                        ]
                    ]
                ]
            ]
        ]


viewSelect : (String -> Msg) -> String -> List Option -> String -> Html Msg
viewSelect command current list icon_class =
    p [ class "control has-icons-left" ]
        [ span
            [ classList
                [ ( "select", True )
                , ( "is-primary", current /= "" )
                ]
            ]
            [ select
                [ onInput command
                ]
                (List.map (viewOption current) list)
            ]
        , span [ class "icon is-small is-left" ]
            [ i [ class icon_class ] []
            ]
        ]


viewOption : String -> Option -> Html Msg
viewOption current select =
    option
        [ value select.value
        , selected (current == select.value)
        ]
        [ text select.text ]


viewResults : Model -> Html Msg
viewResults model =
    table [ class "table is-striped is-hoverable is-fullwidth" ]
        [ thead []
            [ tr []
                [ th [] [ text "Username" ]
                , th [] [ text "First Name" ]
                , th [] [ text "Last Name" ]
                , th [] [ text "Staff?" ]
                ]
            ]
        , tbody [] (List.map viewUser model.usersList.results)
        ]


viewUser : User -> Html Msg
viewUser user =
    tr []
        [ th [] [ text user.username ]
        , th [] [ text user.first_name ]
        , th [] [ text user.last_name ]
        , th []
            [ if user.is_staff then
                span [ class "icon has-text-success" ]
                    [ i [ class "fas fa-check-circle" ] []
                    ]

              else
                span [ class "icon has-text-danger" ]
                    [ i [ class "fas fa-times-circle" ] []
                    ]
            ]
        ]


viewError : Model -> Html Msg
viewError model =
    div [ class "notification is-danger" ]
        [ button [ class "delete" ] []
        , text model.message
        ]


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        InputChanged value ->
            update FormSubmitted { model | searchTerms = value }

        LimitChanged value ->
            update FormSubmitted { model | limit = value }

        IsStaffChanged value ->
            update FormSubmitted { model | isStaff = value }

        OrderingChanged value ->
            update FormSubmitted { model | ordering = value }

        FormSubmitted ->
            ( { model | loading = True }, getUsersList model )

        ResponseReceived (Ok usersList) ->
            ( { model | usersList = usersList, loading = False }, Cmd.none )

        ResponseReceived (Err _) ->
            ( { model | message = "Communication error", loading = False }, Cmd.none )

        ClearFilters ->
            update FormSubmitted initialModel


getUsersList : Model -> Cmd Msg
getUsersList model =
    Http.get
        { url =
            crossOrigin
                "http://127.0.0.1:8000"
                [ "api", "v1", "users" ]
                (getQueryParameterList model)
        , expect = Http.expectJson ResponseReceived usersListDecoder
        }


getQueryParameterList : Model -> List QueryParameter
getQueryParameterList model =
    []
        |> appendSearchParameter model.searchTerms
        |> appendLimitParameter model.limit
        |> appendOrderingParameter model.ordering
        |> appendIsStaffParameter model.isStaff


appendIsStaffParameter : String -> List QueryParameter -> List QueryParameter
appendIsStaffParameter value list =
    case value of
        "true" ->
            UB.string "is_staff" "true" :: list

        "false" ->
            UB.string "is_staff" "false" :: list

        _ ->
            list



{-
   appendOrderingParameter : Ordering -> List QueryParameter -> List QueryParameter
   appendOrderingParameter maybe list =
       case maybe of
           UsernameAscending ->
               UB.string "ordering" "username" :: list

           UsernameDescending ->
               UB.string "ordering" "-username" :: list

           FirstNameAscending ->
               UB.string "ordering" "first_name" :: list

           FirstNameDescending ->
               UB.string "ordering" "-first_name" :: list

           LastNameAscending ->
               UB.string "ordering" "last_name" :: list

           LastNameDescending ->
               UB.string "ordering" "-last_name" :: list

           Default ->
               list
-}


appendSearchParameter : String -> List QueryParameter -> List QueryParameter
appendSearchParameter value list =
    case value of
        "" ->
            list

        _ ->
            UB.string "search" value :: list


appendOrderingParameter : String -> List QueryParameter -> List QueryParameter
appendOrderingParameter value list =
    if List.member value [ "username", "-username", "first_name", "-first_name", "last_name", "-last_name" ] then
        UB.string "ordering" value :: list

    else
        list


appendLimitParameter : String -> List QueryParameter -> List QueryParameter
appendLimitParameter value list =
    if List.member value [ "5", "10" ] then
        UB.string "limit" value :: list

    else
        list


userDecoder : Decoder User
userDecoder =
    map4 User
        (field "username" JD.string)
        (field "first_name" JD.string)
        (field "last_name" JD.string)
        (field "is_staff" JD.bool)


personListDecoder : Decoder (List User)
personListDecoder =
    JD.list userDecoder


usersListDecoder : Decoder UsersList
usersListDecoder =
    map2 UsersList
        (field "count" int)
        (field "results" personListDecoder)


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none
