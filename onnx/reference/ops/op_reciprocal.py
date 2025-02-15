# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunUnaryNum


class Reciprocal(OpRunUnaryNum):
    def _run(self, x):  # type: ignore
        with np.errstate(divide="ignore"):
            return (np.reciprocal(x).astype(x.dtype),)
