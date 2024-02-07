# BR Logic API

Welcome. This is a collaboration between Copper (FateUnix29 / @destiny_29) and I (Perru / @perru_)
This project allows you to create logic-focused creations in the steam game BrickRigs though pseudo-code.
This project is still under developement and isn't fonctional yet.

Here's an exemple of what code would look like:

```
setup {
    fileName = "testDoNotDelete"
    fileDescription = ""
    codeVersion = "A1"
    centerPosition = [0, 0, 0]
    centerRotation = [90, 0, 0]
}

import if
import fpsSensor

myswitch = Switch(inputScale = [0, 1, 1, -1])
newswitch = Switch()

if (myswitch > 0) {
    return(newswitch, 1)
}
```
