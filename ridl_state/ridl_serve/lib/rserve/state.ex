defmodule Rserve.UserState do
   use GenServer
   require IEx

   def start_link(args) do
     name=Map.get(args,"name")
    {:ok,pid} = GenServer.start(__MODULE__,args,[name])
   end

  def init(state) do
    table = :ets.new(:generic_table, [:set, :private])
    state = Map.put(state, :table, table)
    {:ok,state}
  end

 def handle_call({:save_info, params}, _from, state) do
    key = Map.get(params, "key")
    val = Map.get(params, "value")
    table = Map.get(state, :table)

    case :ets.insert(table, {key, val}) do
      true ->
        return_dict = %{"cmd" => "save_info", "val" => "completed"}
        {:reply, return_dict, state}

      _ ->
        return_dict = %{"cmd" => "save_info", "val" => "could not insert"}
        {:reply, return_dict, state}
    end
  end

end
