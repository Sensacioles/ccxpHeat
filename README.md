# ccxpHeat - Sticker Fetching Heatmap

The 2022 edition of CCXP, or Comic-Con Experience, was going on for some days in São Paulo, Brazil. My best friend went to the event and said they were giving free sticker albumns, featuring the artists present there, for people to walk around, collect stickers and give more acknowledgement to those hard-working artists.
My friend showed me she was missing some stickers, so I wrote this algorithm to help her track the places she would find more stickers to collect.
Special thanks in advance to her. Thanks, Sophia! :)


## CCXP Stand Distribution

To be absolutely honest, the convetion map is an absolute mess. I'm not speaking in a attendee way, but from a computer, statistical perspective. Basically, there are 2 sets of rows, for each "area" from A to H, with 22 stands in each set. To save some space, the staff decided to split the areas in two groups of 4, A to D being the left section and E to H the right one. So, to save EVEN MORE space, they came up with the idea to stick the two sets of stands right below one another.

<p align="center">
    <img width="640" src="https://i.imgur.com/HZdZbPx.png" alt="CCXP Artist Stands Map">
</p>

This creates a structural mess, as you can't quite distribute the stands evenly in rows x columns. Knowing this, I created some liberties while coding:
* Divided each area into 'Top' and 'Bottom' rows;
* The number of the top rows are actually one number short to the real stand, the ***stand 1*** in the convention is the ***stand 0*** in the heatmap, the bottom rows numbers are not displayed at all;
* Assigned the middle, empty, space between the rows as a "zero" stand; 
* Transposed the dataframe so it would match the map (spoilers!)

## Methodology

Firstly, a dictionary named `stickersLocations` was created, containing all the stands, for each area, that had remaining stickers to collect. These don't need to be ordered for the code to work properly. Then the number of occurencies of each stand was calculated and assigned to its position in the top and bottom rows.
With the frequency of each stand, they were assigned to top and bottom labels inside another dictionary called `stickerDensity`. The occurency dictionary was used to create the dataframe `dfLocations`, which was trasnposed and split into `transposedLeft` and `transposedRight`.
Two heatmaps were created based on these two slices, `leftHeat` and `rightHeat`, and their plot images were saved. Finally, both images were concatenated into a new image that resembled more CCXP's map on the sticker album.

## Results

With the final heatmap plotted, anyone can see which areas they're missing the most stickers and prioritize them as they see fit, this could help avoid waiting in line for too long and actually miss other stickers they could've grabbed earlier.

<p align="center">
    <img width="1280" src="https://github.com/Sensacioles/ccxpHeat/blob/master/ccxpHeat.png" alt="CCXP Heatmap based on Sophia's missing stickers. Thanks again!">
</p>
