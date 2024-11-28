from flwr.common import Context, ndarrays_to_parameters
from flwr.server import ServerApp, ServerAppComponents, ServerConfig
from flwr.server.strategy import FedAvg

from task import get_params, get_model

def server_fn(context: Context) -> ServerAppComponents:
    """
        Construct components for ServerApp
    """
    num_rounds = context.run_config["num-server-rounds"]
    config = ServerConfig(num_rounds=num_rounds)

    # Setting global model initialization
    model_name = context.run_config["model-name"]
    ndarrays = get_params(get_model(model_name))
    global_model_init = ndarrays_to_parameters(ndarrays)

    # Define strategy
    fraction_fit = context.run_config["fraction-fit"]
    fraction_evaluate = context.run_config["fraction-evaluate"]
    strategy = FedAvg(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        initial_parameters=global_model_init
    )

    return ServerAppComponents(config=config, strategy=strategy)

app = ServerAppComponents(server_fn=server_fn)