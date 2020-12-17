from django import template


register = template.Library()

@register.simple_tag()
def about_us():
    return """
            <div class="about-us" > <!-- Wrapper -->
                <div style="text-align: center"><img src="/static/logo.png" style="position: relative; float: right; margin-top: 90px" width="100%"></div>
                <div style="text-align: left; color: white; font-size: 12pt;" id="about-us-words">
                    <h1 style="font-family: 'Merriweather', serif;">We are Sky Blue Entertainment Company</h1>
                    <p>Sky Blue Entertainment Company was formally established in 2020. Its main business includes music production, artist management. In addition to music, it is also responsible for film production, as well as multimedia.</p>
                    <p>We hope our life can be different. No one can know how long our life is, and what will happen in the future. Since we have our heart to do music and film production, we are not going to postpone, and do it right now.</p>
                    <p>Blue is the colour of sky. For me, sky is representing dreams. So our name is ‘Sky Blue Entertainment Company’, hope to use this name to remind everyone that we must be always full of dreams and whether in a valley or despair, stick to our dreams. As long as you stick to it, your dream will come true one day.</p>
                </div>
            </div>
            <style>
                .about-us {
                    width: 100%;
                    grid-template-columns: 40% 60%;
                    display: inline-grid;
                    grid-gap: 20px;
                    padding-top: 50px;
                    margin: 0;
                }
            </style>
            """

