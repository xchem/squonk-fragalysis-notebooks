# Jupyter notebook images

## Building

```
docker compose build
```

## Local testing

```
docker run -p 8888:8888 maxwinokan/jupyter-fff
```

## Pushing to Dockerhub

```
docker compose push
```

### HIPPO test:

```
!conda list | grep -E "chemicalite|rdkit"
```

```
import hippo
animal = hippo.HIPPO("test", "test.sqlite")
animal.register_compound(smiles="COc1ccc2sc(N)nc2c1")
print(animal.C1)
animal.C1.mol
```

import molparse as mp
import plotly.graph_objects as go
mp.write("test.pdf", go.Figure())