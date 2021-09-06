defmodule RidlStateServer.Repo do
  use Ecto.Repo,
    otp_app: :ridl_state_server,
    adapter: Ecto.Adapters.Postgres
end
