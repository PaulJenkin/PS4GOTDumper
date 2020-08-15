# PS4GOTDumper
Dupes the GOT address of the PS4 in a synchronous way, and let you the adress jumps of each block


# Supported firmwares 
tested till 6.72 should support above as well

# Requirements
1. GOT base address drived from webkit.elf
1. Web server with php support
2. python3 - required to find the base address of the jumps of each blocks


# Setps to run
1. The got base address needs to updated in dump_got.js on line 11, this address comes from objdump of webkit.elf
2. Add these files to web server and launch it
3. This  will create a file called "baseAddress.txt" in the same directory which will have all the address.
4. This will take alteas a 2 to 3 minutes to complete, you will alerted in ps4 once its completed
5. Now you can run the following command "python3 baseJumps.py" (in same directory), this will find the address jumps of each blocks and print it in the screen

# Note
1. If the "baseAddress.txt" file has "!decrement" text in it. then it inicates base address need to be adjusted
2. for example if you have used "10054456" as base GOT address and you see "!decrement" 5 times in the file, you have add 80 toward the base
3. logic is for each "!decrement" add 16 to wards the base
4. So your correct GOT base would be 10054536 (10054456 +16 +16 +16 +16 +16)
5. Repeat the steps 2 to 4 to get a "baseAddress.txt" with any "!decrement" value in it

# Credits
[sleirsgoevy](https://github.com/sleirsgoevy) for base dupmer JS file
