 import numpy as np
 import sys
+import os

 ext_modules = [
     Extension(
         "pycodec2.pycodec2",
         ["pycodec2/pycodec2.pyx"],
-        include_dirs=[np.get_include()],
+        include_dirs=[
+            np.get_include(),
+            os.path.join(os.path.dirname(__file__), "include"),
+        ],
         define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_26_API_VERSION")],
         library_dirs=["lib_win"] if sys.platform == "win32" else None,
         libraries=["libcodec2"] if sys.platform == "win32" else ["codec2"],
     )
 ]
