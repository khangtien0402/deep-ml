import numpy as np


def gradient_direction_magnitude(gradient: list) -> dict:
    gradientss=np.array(gradient,dtype=float)
    magnitude=float(np.linalg.norm(gradientss))
    if magnitude==0.0:
        return {"magnitude":0.0,
                "direction":(gradientss*0).tolist(),
                "descent_direction":(gradientss*0).tolist(),

                }
    else:
        return {"magnitude":magnitude,
                "direction":(gradientss/magnitude).tolist(),
                "descent_direction":(gradientss/-magnitude).tolist()}