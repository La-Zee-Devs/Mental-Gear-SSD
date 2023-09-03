# Debug
label debug:
    menu:
        "Text tags":
            call .text_tags
    return

label .text_tags:
    
    "Text tags:"
    "{b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, {u}underlined{/u}, {alpha=.5}translucent{/alpha}, {color=#0080c0}color{/color}."
    "{a=https://www.renpy.org}link to a website{/a} or {a=jump:credits}jump to a label{/a}."
    "The cps tag controls text typing speed:\nIt can type {cps=25}as an absolute value{/cps}"
    "Or it can type relative to the default speed - {cps=*2}doubling the default speed{/cps} or {cps=*0.5}halving the default speed{/cps}."
    "{font=DejaVuSans-Bold.ttf}DejaVuSans-Bold.ttf{/font}."
    "Kerning: {k=-.5}closer together{/k} or {k=.5}farther apart{/k}."
    "Size: {size=30}Absolute size{/size} or relative size - {size=+10}bigger{/size} or {size=-10}smaller{/size}."
    "Horizontal space in text: {space=30} and {vspace=30}Vertical space between lines."
    "Wait tag (click): {w} (time) {w=.5} final text."
    "Paragraph break = wait tag but with newline - Click: {p}Time: {p=1.5}Newline text."

    "No wait tag to skip slow text{nw}"
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    extend " to the next statement."

    $ variable = "{i}variable value{/i}"
    "Interpolate variables: [variable], interpolate raw variable text without rendering text tags: [variable!q]."
    "For example, this displays the [variable]."
 
    "Escaping in text:  \\: \\\\,  \': \\\',  \": \\\",  {{: {{{{,  [[: [[[["
    "Escaping in dialogue only (not text):  %%: %%%%"

    return

