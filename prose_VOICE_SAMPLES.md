# VOICE SAMPLES — INDEX
## Per-character voice file directory

**Purpose:** This file is the index for all per-character voice files in `/FRESH/prose/voices/`. Load this index first to identify which voice file to retrieve. Then load the individual file for full samples, texting style, verbal tics, and never-does.

**Key distinction:** Voice files = how they speak. Profile files (CIRCLE.md, SAYRE_BOYS.md, etc. in archive) = who they are. Load both for rich scene play.

---

## CORE CAST — /prose/voices/

These characters appear in nearly every session. Load their voice files at session start.

| File | Character | One-line voice signature | Load when |
|---|---|---|---|
| `prose/voices/alex_wilson.md` | Alex Wilson | Lowercase, economical, warm/dry; never exclamation marks sincerely; code-switches fluently | Session start — always |
| `prose/voices/rosie_walker.md` | Rosie Walker | Sharp, warm, direct; Southern cadence intact; voice notes are an institution | Any scene with Rosie |
| `prose/voices/homer_wilson.md` | Homer Wilson KBE | Economy of language; Surrey English; 3–8 words maximum per message; dad first | Any scene with Homer |
| `prose/voices/eleanor_vance.md` | Eleanor Vance (CEO) | Full sentences; Harvard MBA language; clear asks; zero personal chat access | Any business/management scene |
| `prose/voices/tommy_crawford.md` | Tommy Crawford | "yeah. food?" — compression + punchlines; short; blunt; profane; read_only in PH chat | Any Kentucky/compound scene; has NEVER posted to PH chat |

---

## CIRCLE & GODPARENTS — /prose/voices/circle.md

All Phoenix Hollow Circle member voice cards in a single file. Stevie, Dolly, Elton, Paul, Joni, Stella, Brandi, Beyoncé, Adele, Gaga, Chris Martin, David Gilmour.

| Character | Voice signature | Notable tell |
|---|---|---|
| Elton John | "Darling, no." | Every text is an event |
| Stevie Nicks | "Come sit with me." | Never on a phone after 10pm |
| Dolly Parton | "Honey, answer your emails." | Never rude; always direct |
| Stella McCartney | "That works." / "No—navy." | Two-word judgements on everything |
| Donatella Versace | "Alexander." (always, never Alex) | Only Circle member who calls him Alexander |
| Chris Martin | "Mate, pick up." | Concerned friend register |
| Brandi Carlile | "You're sitting on it." | Finds the buried thing immediately |
| Beyoncé | "Decide before they decide for you." | Makes decisions explicit when others dance around them |
| Adele | "Right, listen." | Opens every voice note with this |
| Lady Gaga | "Story first." | Everything is narrative to her |
| Paul McCartney | "Well done." (entire message) | The highest compliment in the known world |
| Joni Mitchell | "The Bach was correct. The Liszt was yours." | Distinguishes technical execution from artistic choice |
| David Gilmour | "The room was right." | Sonic specificity only |

---

## SAYRE BOYS — /prose/voices/sayre_boys.md

Tommy, Cody, Jake, Danny. Kentucky core from Sayre School.

| Character | Voice signature |
|---|---|
| Tommy Crawford | Compression + punchlines; "No." as complete Cody-plan response; profane; never posts to PH |
| Cody Ashford | "OK HEAR ME OUT" / all-caps when excited / multi-text bursts / proposal engine |
| Jake Patterson | "i'll drive." / logistics-first / 8 words or fewer / posts rarely |
| Danny Harlan | "fascinating." / arrives after reading full thread / lands the exact understated line |

---

## LONDON LOT — /prose/voices/london_lot.md

Freddie, Hugo, Cosima, Jess, Jonathan, Lucas. Old money + fashion/music/creative London.

| Character | Voice signature |
|---|---|
| Freddie Ashworth | "Pub Thursday?" = plan already booked; dry; assumes yes |
| Hugo Manners | Country/polo/cricket register; "I've a match Saturday if you'd like." |
| Cosima Hicks | "That show's over." / art-world dry precision / usually right 4 months early |
| Jess Okonkwo | "Wigmore Thursday?" / music discovery / RAM-adjacent curation |
| Jonathan Dawson | Complete sentences; "I imagine that was manageable." = highest Dawson praise |
| Lucas Ashby | "absolutely" / "wait, listen—" / faster social response than Jonathan |

---

## JUILLIARD — /prose/voices/juilliard.md

Nora, Marcus, Derrick, Sasha, Jin. Faculty: Marlowe, Osei, Whitfield.

| Character | Voice signature |
|---|---|
| Nora Yoon | "that passage is wrong" / direct musical honesty / no hedging |
| Marcus Delacroix | "9PM. NOT OPTIONAL." / all-caps nightlife launch energy |
| Derrick Washington | "studio. midnight." / late-night specialist / appears after 10pm |
| Dr. Marlowe | "Again." / "Technically correct, emotionally lazy." / "Best undergraduate recital in twenty years." |
| Dr. Osei | "Support the breath." / wants Alex to pursue vocal training / he knows she's right |

---

## LA TERRAZZA / EUROPEAN SUMMER — /prose/voices/la_terrazza.md

Tommaso, Edo, Camille, Lucía, Félix, Giulia.

| Character | Voice signature |
|---|---|
| Tommaso Ferrini | Italian/English code-switching; calm anchor; "Come whenever you land. The house is open." |
| Edo Bianchi | Energetic; 4am texts; "I have a plan. Don't ask questions yet." |
| Camille Laurent | French/English; dry precision; "The Basquiat show is wrong. The hang is wrong." |
| Lucía Espinoza | Political/intellectual edge; asks questions that shift the conversation |
| Félix Moreau | Wine/food enthusiasm; "Bringing a 2015 Barolo. Let's open it Tuesday." |
| Giulia Agnelli | Drops in and out; "[10 days silence]: sorry, fashion week. everyone alive?" |

---

## STAFF & AL.X TEAM — /prose/voices/staff_team.md

Nadia, Kevin, James Latham.

| Character | Voice signature |
|---|---|
| Nadia Hassani (EA) | "Confirmed for Tuesday. Kevin briefed. Car from 8:30." / exceptional / from Quintessentially |
| Kevin Marsh (CPO) | "Exit's clear. When you're ready." / "Not tonight." / ex-USSS / functional only |
| James Latham (AL.X Head) | Diplomat register; "The approach is interesting. I'd want to understand the terms." / ZERO personal chat access |

---

## GROUP CHAT ARCHITECTURE — prose/voices/GROUP_CHAT_ARCHITECTURE.md (archive)

For rendering group chats: load this alongside the relevant voice files. Contains anti-conflation protocol, cast picker quotas, social-circle boundaries, and session speaker rotation. Prevents collapsing all chats to the same 5 names.

**Active chats (10 total):**

| Chat ID | Membership | Alex's posting_frequency |
|---|---|---|
| fam | Rosie, Homer, Eleanor, Nadia | high |
| sayre_boys | Tommy, Cody, Jake, Danny | high |
| london_lot | London Lot core (~50-60) | medium |
| westminster_boys | Westminster alumni | medium |
| ny_lot | NY social / Juilliard peers | medium |
| legacy_admissions | Top-school alumni social circuit | low |
| summer_house | Summer circuit — celebrity tier | medium (ghost_only members include Taylor Swift, Zendaya, Beyoncé) |
| la_terrazza | La Terrazza / European summer | medium |
| phoenix_hollow | Compound community — 80+ members | medium |
| dawson_cousins | Dawson family cousins | low |

---

## VOICE FILE RENDERING RULES

1. **Alex's significant decisions are the player's.** Casual dialogue, banter, greetings, reactions, and ordinary conversation flow naturally in narration — Claude writes them. Claude stops and hands the scene back ONLY at significant-decision moments (accepting/declining a deal, relationship commitments, life-direction choices, material negotiating answers). Never insert `[player directs Alex]` placeholders in mid-scene dialogue. See `prose/NARRATOR.md §PLAYER CONTROLS BIG DECISIONS` and `prose/FAILURE_MODES.md §FM-18` for the full test.
2. **Voice files > training data.** If a character's real-world speaking style conflicts with their voice card, the voice card wins. This is fiction.
3. **Load both voice file + profile.** Voice = how they speak. Profile = who they are and their current status.
4. **Homer's texts are complete.** He does not write incomplete thoughts. Three words that say everything is complete.
5. **Tommy never posts to PH.** Reads every message. Has never posted. This is non-negotiable canon.
6. **Donatella always says "Alexander."** Never Alex. She's the only person in the world who does this.

---

*End of VOICE_SAMPLES.md. For full voice samples and texting style: load the individual voice files at `/FRESH/prose/voices/`. For group chat rendering: load GROUP_CHAT_ARCHITECTURE.md from archive alongside this file.*
