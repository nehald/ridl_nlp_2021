defmodule RserveWeb.PageController do
  use RserveWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
