defmodule Rserve.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Start the Telemetry supervisor
      RserveWeb.Telemetry,
      # Start the PubSub system
      {Phoenix.PubSub, name: Rserve.PubSub},
      # Start the Endpoint (http/https)
      RserveWeb.Endpoint
      # Start a worker by calling: Rserve.Worker.start_link(arg)
      # {Rserve.Worker, arg}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Rserve.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    RserveWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
