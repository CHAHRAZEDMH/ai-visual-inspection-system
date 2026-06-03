from anomalib.data import MVTecAD
from anomalib.models import Patchcore
from anomalib.engine import Engine

DATASET_ROOT = r"C:\Users\chahr\Desktop\Projects\ai-visual-inspection-system\data\mvtec_anomaly_detection"

datamodule = MVTecAD(
    root=DATASET_ROOT,
    category="capsule",
    train_batch_size=8,
    eval_batch_size=8,
    num_workers=0,
)

model = Patchcore()

engine = Engine(
    max_epochs=1,
    accelerator="gpu",
    devices=1,
)

engine.fit(
    model=model,
    datamodule=datamodule,
)

engine.test(
    model=model,
    datamodule=datamodule,
)