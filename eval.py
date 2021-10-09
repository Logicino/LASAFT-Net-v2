import dotenv
import hydra
from omegaconf import DictConfig, OmegaConf
from pytorch_lightning.utilities.distributed import rank_zero_info

from src.source_separation.conditioned.scripts import evaluator

dotenv.load_dotenv(override=True)


def main(cfg: DictConfig):
    # Load config
    rank_zero_info(OmegaConf.to_yaml(cfg))

    evaluator.eval(cfg)


@hydra.main(config_path="conf", config_name="eval")
def hydra_entry(cfg: DictConfig) -> None:
    main(cfg)


if __name__ == '__main__':
    hydra_entry()
