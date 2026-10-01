"""Toy trainer entry point (the real model code lives on the cluster)."""
import argparse
import yaml


def load_config(path):
    with open(path) as f:
        cfg = yaml.safe_load(f)
    return cfg


def build_optimizer(cfg):
    lr = float(cfg["lr"])
    warmup = int(cfg["warmup_steps"])
    return {"type": "adamw", "lr": lr, "warmup": warmup}


def build_eval_optimizer(cfg):
    lr = float(cfg["lr"])
    warmup = int(cfg["warmup_steps"])
    return {"type": "adamw", "lr": lr, "warmup": warmup}


def train(cfg):
    opt = build_optimizer(cfg)
    for step in range(cfg["max_steps"]):
        loss = step_fn(cfg, opt, step)
        if step % 250 == 0:
            print(f"step {step:5d} loss {loss:.4f} lr {opt['lr']}")


def step_fn(cfg, opt, step):
    return 2.9 / (1 + step / 1000)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/base.yaml")
    train(load_config(p.parse_args().config))
