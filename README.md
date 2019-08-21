## palach-game
##### A hangman \(or "palach"\) game to practice Russian \(and English\) vocabulary. 

### About

This is your standard hangman game, but intended to be played in a non-native language \(it's for me, so primarily Russian, but there is an ESL option too\) for vocabulary practice.  The game takes its word choices from a vocabulary file, allowing the student to focus on one topic at a time.  Input in Cyrillic works beautifully \(thanks, Unicode!\).

### Current work

The next step is to be able to upgrade from just a vocabulary list to a CSV file that includes hints \(both target-language and English\) and definitions for each word.  This adds a level of language learning beyond just how to spell a word, because it will force the player to come up with the vocab word based on a hint or definition.  The fact that the hint is in the target language is consistent with good language teaching practices, which minimize the use of translations and explanations in L1 \(ie, they're immersion-based\).  The student would then be able to ask for a hint from within the game if they are stumped for a word.

### Future features:

In the future, I would like to include different levels of play.  For example, on the easiest level, the player could get three hints: a target-language explanation, an L1 (native language) explanation, and the L1 translation of the word.  On the hardest level, hints would be totally disabled.  The next hardest would have only target-language hints enabled, &c.  Levels could also vary on how many wrong answers are needed to build the hangman, and on whether the player has access to which letters have already been played.

Additionally, one of the benefits of the setup with CSV files is the ease of adding new languages.  All you would have to do is create a new language file, where the target vocabulary is in column one, the first hint is in column two, &c.  The program could be pointed towards this file and would not need to be edited or changed in any way.  In the future I would like to add French and Spanish, but any language with an alphabet or syllabary could be used (it would be interesting to try with an abjad, but I think it would work sub-optimally at best).
