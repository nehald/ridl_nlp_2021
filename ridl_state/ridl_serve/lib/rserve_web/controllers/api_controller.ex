defmodule RserveWeb.ApiController do
  use RserveWeb, :controller
  require IEx
  alias Rserve.UserState

  def index(conn, _params) do
    render(conn, "index.html")
  end

  def signin(conn,params) do
     IEx.pry
     UserState.start_link(params)
     json(conn,%{"hello" => "desai"})
  end
end
