

def get_environment(env_name):
    try:
        if env_name in ('tictactoe'):
            from environments.tictactoe.tictactoe.envs.tictactoe import TicTacToeEnv
            return TicTacToeEnv
        elif env_name in ('Football'):
            from environments.Football.Football.envs.Football import modf_football
            return modf_football
        elif env_name in ('connect4'):
            from environments.connect4.connect4.envs.connect4 import Connect4Env
            return Connect4Env
        elif env_name in ('sushigo'):
            from environments.sushigo.sushigo.envs.sushigo import SushiGoEnv
            return SushiGoEnv
        elif env_name in ('butterfly'):
            from environments.butterfly.butterfly.envs.butterfly import ButterflyEnv
            return ButterflyEnv
        elif env_name in ('geschenkt'):
            from environments.geschenkt.geschenkt.envs.geschenkt import GeschenktEnv
            return GeschenktEnv
        else:
            raise Exception(f'No environment found for {env_name}')
    except SyntaxError as e:
        print(e)
        raise Exception(f'Syntax Error for {env_name}!')
    except:
        raise Exception(f'Install the environment first using: \nbash scripts/install_env.sh {env_name}\nAlso ensure the environment is added to /utils/register.py')
    


def get_network_arch(env_name):
    if env_name in ('tictactoe'):
        from models.tictactoe.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('Football'):
        from models.Football.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('connect4'):
        from models.connect4.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('sushigo'):
        from models.sushigo.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('butterfly'):
        from models.butterfly.models import CustomPolicy
        return CustomPolicy
    elif env_name in ('geschenkt'):
        from models.geschenkt.models import CustomPolicy
        return CustomPolicy
    else:
        raise Exception(f'No model architectures found for {env_name}')

