# Spookifying Lovecraft
## Replacing all the adjectives in Lovecraft with 'spooky'

As Myths Retold said:

```
oh by the way
fun fact
HP Lovecraft is a HUGE FAN OF ADJECTIVES
the more syllables the better
sometimes it can make reading his writing very difficult
but luckily i discovered a trick
which is that you can replace almost every single one of his adjectives
with “spooky”
without any loss of meaning
let’s try it on one of the paragraphs from the sailor’s account!
AHEM:

“I suppose that only a single mountain-top, the spooky, spooky citadel whereon spooky Cthulu was buried,
actually emerged from the waters… Johansen and his men were awed by the spooky majesty of this spooky 
Babylon of spooky demons, and must have guessed without guidance that it was nothing of this or any 
other sane planet. Awe at the spooky size of the spooky stone blocks, at the spooky height of the 
spooky, spooky monolith, and at the spooky identity of the spooky statues and bas-reliefs with the 
spooky image found in the shrine on the Alert, is spookily visible in every line of the mate’s spooky 
description.”
```
[Check out the whole review!](http://bettermyths.com/boats-an-elder-gods-only-weakness/)

So I started thinking, it wouldn't be that hard to make a quick app that replaces all of his adjectives with "spooky".

## Programs Used
* NLTK for adjective identification
* Flask for web application
* hplovecraft.com/writings/texts/

## Instalation
In file ls_app:
* create/run a virtualenv
* `pip install .`
* `export FLASK_APP=ls_app`
* `flask initdb`
* `flask run`