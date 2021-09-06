# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :ridl_state_server,
  ecto_repos: [RidlStateServer.Repo]

# Configures the endpoint
config :ridl_state_server, RidlStateServerWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "hsXnRd2suNm80kHF8vTx50yPg13tV6GZFP5tsYWUnu85D/yCuJTq5VYGB/9LjDjl",
  render_errors: [view: RidlStateServerWeb.ErrorView, accepts: ~w(html json), layout: false],
  pubsub_server: RidlStateServer.PubSub,
  live_view: [signing_salt: "LRTdh96d"]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
