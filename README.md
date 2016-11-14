cryptoc
=======

Cryptographic algorithms implemented for **educational and entertainment purposes**. Should never be used in production for actual real-world cryptographic solutions. No external dependencies, written using _Python 2.7_. Actually made for educational purposes to progressively introduce various concepts from the cryptographic world through various algorithms (status: _alpha_).

Algorithms
----------

- ROT, as in [ROT13](https://en.wikipedia.org/wiki/ROT13), illustration of the translation between a written character and a number and the use of this translation
- xOR, illustration of the infamous [exclusive Or](https://en.wikipedia.org/wiki/Exclusive_or)
- [Affine](https://en.wikipedia.org/wiki/Affine_cipher), illustration of the use of a multi-input mathematical function on letters translated into numbers
- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), illustration of the use of an alphabet and of a modulo operation as a consequence
- [Atbash](https://en.wikipedia.org/wiki/Atbash), illustration of a substitution and of alphabet manipulation (_reversed_ in this specific case)
- [Book](https://en.wikipedia.org/wiki/Book_cipher), illustration of using a specific source (a _"book"_ in this case) as a mask instead of a more expected _"key"_)
- [Vigenere](https://en.wikipedia.org/wiki/Vigenere_cipher), illustration of the use of the use of a keystream with initialization
- [Autokey](https://en.wikipedia.org/wiki/Autokey_cipher), illustration of the use of a buffer and feedbacks/loops in cryptographic algorithms
- [Vernam](https://en.wikipedia.org/wiki/Gilbert_Vernam#The_Vernam_cipher), illustration of a combination of previous illustrations as a way to craft cryptographic algorithms
- [Railfence](https://en.wikipedia.org/wiki/Rail_fence_cipher), illustration of moving elements' positions and orders
- ARC4, the alleged [RC4](https://en.wikipedia.org/wiki/RC4), illustration of the use of pseudo-randomness generation and key scheduling
- [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), illustration of the use of stronger mathematical concepts and of public/private keys
- [Keyword](https://en.wikipedia.org/wiki/Keyword_cipher), illustration of alphabet letters' order manipulation

Todo
----

- Unified testing library, enjoying the fact that most of the tests are identical and categories of inputs and outputs can be easily mapped
- Better educational value through smarter commenting, more detailed explanations in the README.md and so forth
- Add new algorithms
- Extend it with a sister-project _pocpression_ (or _enpocding_ maybe ?)
- Provide a framework to toy around with various illustrated cryptographic operations/sub-functions