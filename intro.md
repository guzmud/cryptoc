# cryptoc (*working title*)

Cryptography, or the art of writing secrets through secret writings, seems to have appeared only a few centuries after writing itself. Secrecy, as a tool, is a natural part of the human trades. Then, one century after an other, cryptography evolved and from it stemmed various sciences during the modern era :
* *cryptography*, itself as the practice of encoding secrets
* *cryptanalysis*, as the practice of bypassing cryptography through analysis
* *cryptology*, as the theorized science behind both -graphy and -analysis
* *cryptosystem engineering*, to cite just one more

As a rule of thumb, based on the various best-sellers on the subject and student courses, cryptography is studied along two, usually mutually exclusive, lines
* cryptography as a *science*, mostly regarding the internals (a.k.a. maths, and information theory too, let's not forget it)
* cryptography as a *tool*, usually in engineering context (mostly, communications and information systems)

Both of those paths are more than legit, and, when well done, admirable and enjoyable (although as most things in life, joy may not be perceived or shared by each and anyone, alas). There is neverless an other path that may be worth walking and that may, if properly done, lead to opening a new door into cryptography. A door as in a new access to it, an access as in a bridge into cryptography for a slightly (but usually overlapping) public. A path where the objective is neither to have the mastery of a cryptographer nor the tooling for engineery, but to simply satisfy the curiosity of some of the autodidacts amongst us that may find through it way more than a door into cryptography, but into new ideas and problematics larger than what a simple book could cover.

This book is a shot at it, at opening this door. This book is an expedition along this path, trying to turn personal experiences of autodidact cryptography discovery into a shareable and enjoyable knowledge. This book is about one thing : neither about maths, neither about code, nor about engineering ; it's all about savoring the exquisite art of cryptography (with a bit of cryptanalysis concern, as both are interlinked, but, with all due respect, this work will not be sciency enough for cryptology eligibility).


## The truth behind the spoon

Before anything, a first bit of information (*pun intended*) :
> **everything is information**

Anything else is just a question of formatting, presenting, interpreting. Whether in a binary form, using numbers, letters, sigils, whatever : it definitely is information and, lucky for us, information is at the heart of our subject.

### First mathematical pit stop

Each of those formats, casted into symbols, forms a whole universe of sort, from which it is possible to jump into an other one according to the rules of translation between. The usual example is, on one hand, the extended ASCII and, on the other hand, a ring going from 0 to 255. Thanks to the bijectivity between both, artificially created using a mapping between an ASCII symbol and an element of modulo 255 ring, one of the bridges between the human and the machine universe has been built.

### tl;dr
* **information**
* **presenting**
* **universe**


## The essence of cryptography

Cryptography aims at taking an original information (let's name it *cleartext*) and to turn it into a different one (let's name it *cyphertext*). Uses are multiple, although mostly regarding storing and sharing, but the main trick is the notion of secrecy, the idea of limitation of access to the original information to unwanted individuals through representation manipulation.

And from there, dear readers, the whole path is a charming bucolic walk, observing the internal machinery invented and reinvented through the ages in order to further this goal of secrecy.

### tl;dr
* **cleartext**
* **cyphertext**


From this point, each chapter will cover an algorithm 
