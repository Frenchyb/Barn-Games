# Barn Games

Little farm games for Violet.

- `day-on-the-farm/`: Day on the Farm, a show to watch. Morning, Feeding Time, Muddy Pig Bath, Round-Up, Mama and Baby, and Bedtime, with a narrator voice. Tap any animal and it says hello.
- `barnyard-race/`: the Barnyard Race.

Both load three.js from a CDN and share the animal models and sounds in `barnyard-race/models` and `barnyard-race/sounds` (credits in `barnyard-race/CREDITS.md`). To open them, serve the repo (`python3 -m http.server`) and visit the game's folder, or make a single file that opens straight from disk:

    python3 tools/bundle.py day-on-the-farm/index.html day-on-the-farm.html
