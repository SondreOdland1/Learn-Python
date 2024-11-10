import pygame
import random
import os

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (144, 238, 144)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (200, 0, 0)
DARK_YELLOW = (200, 200, 0)
DARK_BLUE = (0, 0, 200)

# Screen setup
WIDTH, HEIGHT = 1400, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flashcard Game')

# Font
font = pygame.font.SysFont(None, 48)

# Flashcards with both text and images in the same card (if needed)
flashcards = [
    {'question': 'What is the formula to calculate the risk-free rate of return for a zero-coupon bond, and how is it applied?', 'answer': ['This formula is used to determine the return an investor can expect if they hold the bond until maturity, assuming no risk of default, making it useful for calculating the return on government-issued securities like treasury bonds.', 'image: risk-free rate of return for a zero-coupon bond.png'], 'repeats': 1},
    
    {'question': 'How do you calculate the price of a bond with periodic interest payments?', 'answer': ['This formula discounts all future cash flows (coupon payments and the final face value) to their present value.', 'image: Price of a bond with periodic coupon payments.png'], 'repeats': 1},
    
    {'question': 'What is the difference between a coupon bond and a zero-coupon bond?', 'answer': ['''A coupon bond makes regular interest payments (coupons) to the holder until maturity, where the face value is also paid. The price of a coupon bond is calculated by summing the present value of all future coupon payments and the final face value at maturity. 
                                                                                                    
                                                                                                     A zero-coupon bond, on the other hand, does not make periodic interest payments. Instead, it is sold at a discount to its face value, and the investor receives the face value at maturity. The return on a zero-coupon bond comes entirely from the difference between the purchase price and the face value.'''], 'repeats': 1},
    
    {'question': 'How is the price of a stock calculated using the Dividend Discount Model (DDM)?', 'answer': ['The Dividend Discount Model (DDM) calculates the price of a stock as the present value of all expected future dividends. This model is based on the assumption that the value of a stock is equal to the present value of all future dividend payments.', 'image: DDM.png'], 'repeats': 1},
    
    {
    'question': 'What is the concept of the time value of money, and how does it relate to discounting?', 
    'answer': ['The time value of money is the principle that a sum of money has greater value today than it will at some point in the future due to its potential earning capacity. This concept underpins the practice of discounting, where future cash flows are adjusted to reflect their present value. This formula is used in bond pricing, stock valuation, and other financial applications.', 'image: PV of cash flow.png'], 
    'repeats': 1
},
{
    'question': 'What is the importance of the risk-free rate in financial models?', 
    'answer': ['The risk-free rate serves as the baseline for determining the required rate of return for investments. It is used in models like CAPM and for discounting future cash flows. Investors compare the risk-free rate with the return on riskier assets to determine whether the additional risk is worth taking.'], 
    'repeats': 1
},
{
    'question': 'Explain the term structure of interest rates and its significance in bond pricing.', 
    'answer': ['The term structure of interest rates, also known as the yield curve, shows the relationship between bond yields and maturities. It impacts bond pricing as the discount rate applied to future cash flows depends on the maturity of the bond. A steep yield curve often indicates rising interest rates in the future.'], 
    'repeats': 1
},
{
    'question': 'How is the required rate of return used in investment decision-making?', 
    'answer': ['The required rate of return represents the minimum return investors expect to achieve, considering risk. It is used to discount future cash flows to their present value, helping investors determine whether to invest in an asset. In CAPM, the required return is based on the risk-free rate, beta, and market premium.'], 
    'repeats': 1
},
{
    'question': 'How does the concept of duration help in managing interest rate risk in bond portfolios?', 
    'answer': ['Duration measures the sensitivity of a bonds price to changes in interest rates. It is the weighted average time to receive the bonds cash flows, and it helps investors understand how much a bonds price will change in response to interest rate fluctuations. The higher the duration, the more sensitive the bond is to interest rate changes. Modified duration provides an approximation of the percentage price change for a 1% change in interest rates. Investors use duration to manage interest rate risk in bond portfolios, balancing bonds with different durations.'], 
    'repeats': 1
},
{
    'question': 'What is the present value of a perpetuity, and when is this formula applied?', 
    'answer': ['A perpetuity is a financial instrument that pays a constant cash flow indefinitely. The present value is calculated using the formula PV = C/r, where C is the constant cash flow and r is the discount rate. This formula is used in valuing assets like preferred stocks or real estate investments.', 'image: PV of perpetuity.png'], 
    'repeats': 1 #Forelesning 2
},

{
    'question': 'What is capital allocation, and why is it important in portfolio management?', 
    'answer': ['', 'image: What is capital allocation, and why is it important in portfolio management?.png'], 
    'repeats': 1
},
{
    'question': 'How does diversification improve a portfolios risk-return balance?', 
    'answer': ['', 'image: How does diversification improve a portfolios risk-return balance?.png '], 
    'repeats': 1
},
{
    'question': 'Explain the relationship between correlation and diversification in portfolio management.', 
    'answer': ['', 'image: Explain the relationship between correlation and diversification in portfolio management..png'], 
    'repeats': 1
},
{
    'question': 'What is covariance, and how does it relate to portfolio risk?', 
    'answer': ['', 'image: What is covariance, and how does it relate to portfolio risk?.png'], 
    'repeats': 1
},
{
    'question': 'How does combining bonds and stocks reduce portfolio risk, even when they are not perfectly correlated?', 
    'answer': ['', 'image: How does combining bonds and stocks reduce portfolio risk, even when they are not perfectly correlated?.png'], 
    'repeats': 1
},
{
    'question': 'What is the expected return of a portfolio, and how is it calculated for a portfolio consisting of bonds and stocks?', 
    'answer': ['', 'image: What is the expected return of a portfolio, and how is it calculated for a portfolio consisting of bonds and stocks?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Sharpe ratio, and how is it improved through diversification?', 
    'answer': ['', 'image: What is the Sharpe ratio, and how is it improved through diversification?.png '], 
    'repeats': 1
},
{
    'question': 'Describe the concept of reducing standard deviation in a diversified portfolio.', 
    'answer': ['', 'image: Describe the concept of reducing standard deviation in a diversified portfolio..png'], 
    'repeats': 1
},
{
    'question': 'What is the significance of correlation in determining the optimal mix of assets for minimizing portfolio risk?', 
    'answer': ['', 'image: What is the significance of correlation in determining the optimal mix of assets for minimizing portfolio risk?.png'], 
    'repeats': 1
},
{
    'question': 'How does correlation between bonds and stocks influence the overall risk in a portfolio?', 
    'answer': ['', 'image: How does correlation between bonds and stocks influence the overall risk in a portfolio?.png'], 
    'repeats': 1 #Forelesning 3 og 4
},
{
    'question': 'What is the Markowitz Portfolio Selection Model, and what does it aim to optimize?', 
    'answer': ['', 'image: What is the Markowitz Portfolio Selection Model, and what does it aim to optimize?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Minimum-Variance Frontier, and how does it differ from the Efficient Frontier?', 
    'answer': ['', 'image: What is the Minimum-Variance Frontier, and how does it differ from the Efficient Frontier?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Global Minimum-Variance Portfolio, and where is it located on the Minimum-Variance Frontier?', 
    'answer': ['', 'image: What is the Global Minimum-Variance Portfolio, and where is it located on the Minimum-Variance Frontier?.png'], 
    'repeats': 1
},
{
    'question': 'How does an investor choose a portfolio on the Efficient Frontier based on risk tolerance?', 
    'answer': ['', 'image: How does an investor choose a portfolio on the Efficient Frontier based on risk tolerance?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Capital Allocation Line (CAL), and what is its relationship with the Efficient Frontier?', 
    'answer': ['', 'image: What is the Capital Allocation Line (CAL), and what is its relationship with the Efficient Frontier?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Tangency Portfolio, and why is it important?', 
    'answer': ['', 'image: What is the Tangency Portfolio, and why is it important?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Separation Principle in the context of portfolio theory?', 
    'answer': ['', 'image: What is the Separation Principle in the context of portfolio theory?.png'], 
    'repeats': 1
},
{
    'question': 'What are the key components of the Single-Index Model (SIM)?', 
    'answer': ['', 'image: What are the key components of the Single-Index Model (SIM)?.png'], 
    'repeats': 1
},
{
    'question': 'What is the difference between systematic and unsystematic risk in the Single-Index Model?', 
    'answer': ['', 'image: What is the difference between systematic and unsystematic risk in the Single-Index Model?.png'], 
    'repeats': 1
},
{
    'question': 'How is the Sharpe ratio calculated, and why is it important in portfolio theory?', 
    'answer': ['', 'image: How is the Sharpe ratio calculated, and why is it important in portfolio theory?.png'], 
    'repeats': 1 #Forelesning 5
},
{
    'question': 'What is the Capital Asset Pricing Model (CAPM), and what are its core assumptions?', 
    'answer': ['', 'image: What is the Capital Asset Pricing Model (CAPM), and what are its core assumptions?.png'], 
    'repeats': 1
},

{
    'question': 'How do investors maximize the Sharpe ratio, and what is its significance in CAPM?', 
    'answer': ['', 'image: How do investors maximize the Sharpe ratio, and what is its significance in CAPM?.png'], 
    'repeats': 1
},
{
    'question': 'What is the tangency portfolio, and why is it important in CAPM?', 
    'answer': ['', 'image: What is the tangency portfolio, and why is it important in CAPM?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Capital Market Line (CML), and how does it relate to the Security Market Line (SML)?', 
    'answer': ['', 'image: What is the Capital Market Line (CML), and how does it relate to the Security Market Line (SML)?.png'], 
    'repeats': 1
},
{
    'question': 'Explain the Security Market Line (SML) and its role in asset pricing under CAPM.', 
    'answer': ['', 'image: Explain the Security Market Line (SML) and its role in asset pricing under CAPM..png'], 
    'repeats': 1
},
{
    'question': 'What is the difference between systematic and idiosyncratic risk in CAPM, and which one matters?', 
    'answer': ['', 'image: What is the difference between systematic and idiosyncratic risk in CAPM, and which one matters?.png'], 
    'repeats': 1
},
{
    'question': 'What is beta, and how is it calculated? Why is it important in CAPM?', 
    'answer': ['', 'image: What is beta, and how is it calculated? Why is it important in CAPM?.png'], 
    'repeats': 1
},
{
    'question': 'How does CAPM explain the concept of lending and borrowing along the CML?', 
    'answer': ['', 'image: How does CAPM explain the concept of lending and borrowing along the CML?.png'], 
    'repeats': 1
},
{
    'question': 'Can a security with a higher standard deviation have a lower expected return in CAPM?', 
    'answer': ['', 'image: Can a security with a higher standard deviation have a lower expected return in CAPM?.png'], 
    'repeats': 1
},
{
    'question': ' How does CAPM ensure market equilibrium, and what role does the market portfolio play?', 
    'answer': ['', 'image:  How does CAPM ensure market equilibrium, and what role does the market portfolio play?.png'], 
    'repeats': 1 #Forelesing 6
},
{
    'question': 'What is the Arbitrage Pricing Theory (APT)?', 
    'answer': ['', 'image: What is the Arbitrage Pricing Theory (APT)?.png'], 
    'repeats': 1
},
{
    'question': 'How does APT differ from CAPM in terms of assumptions?', 
    'answer': ['', 'image: How does APT differ from CAPM in terms of assumptions?.png'], 
    'repeats': 1
},
{
    'question': 'Explain the concept of arbitrage in APT.', 
    'answer': ['', 'image: Explain the concept of arbitrage in APT..png'], 
    'repeats': 1
},
{
    'question': 'What is a multifactor model in finance?', 
    'answer': ['', 'image: What is a multifactor model in finance?.png'], 
    'repeats': 1
},
{
    'question': 'What is the Security Market Line (SML) in a multifactor model?', 
    'answer': ['', 'image: What is the Security Market Line (SML) in a multifactor model?.png'], 
    'repeats': 1
},
{
    'question': 'Why is diversification important in APT?', 
    'answer': ['', 'image: Why is diversification important in APT?.png'], 
    'repeats': 1
},
{
    'question': 'How does APT handle firm-specific risks?', 
    'answer': ['', 'image: How does APT handle firm-specific risks?.png'], 
    'repeats': 1
},
{
    'question': 'What are the risk factors in the Fama-French Three-Factor Model?', 
    'answer': ['', 'image: What are the risk factors in the Fama-French Three-Factor Model?.png'], 
    'repeats': 1
},
{
    'question': 'Explain the arbitrage-free condition in APT.', 
    'answer': ['', 'image: Explain the arbitrage-free condition in APT..png'], 
    'repeats': 1
},
{
    'question': 'What is the role of beta in APT?', 
    'answer': ['', 'image: What is the role of beta in APT?.png'], 
    'repeats': 1 #Forelesing 7
},
{
    'question': 'What is the Efficient Market Hypothesis (EMH) and its significance in finance?', 
    'answer': ['', 'image: What is the Efficient Market Hypothesis (EMH) and its significance in finance?.png'], 
    'repeats': 1
},
{
    'question': 'Explain the Weak Form of the Efficient Market Hypothesis (EMH).', 
    'answer': ['The Weak Form of the EMH asserts that current stock prices fully incorporate all historical trading data, such as prices and volume. Therefore, it is impossible to predict future price movements based on past performance, rendering technical analysis ineffective. This is because price changes follow a random walk, meaning that future price changes are independent of past ones. According to this hypothesis, strategies relying on chart patterns or moving averages to forecast future prices will not work over the long term.', 'image: '], 
    'repeats': 1
},
{
    'question': 'Describe the Semi-Strong Form of EMH and its implications for fundamental analysis.', 
    'answer': ['The Semi-Strong Form of EMH posits that stock prices adjust rapidly to new public information, meaning all publicly available data is reflected in current stock prices. This includes earnings reports, economic news, and corporate announcements. As a result, fundamental analysis, which involves evaluating a company’s financials and prospects, cannot consistently lead to outperformance. The rationale is that once new information is released, the market quickly assimilates it, making it impossible to profit from it before others do. For example, if a company releases positive earnings news, its stock price will instantly adjust to reflect the higher value, leaving no opportunity for arbitrage.', 'image: '], 
    'repeats': 1
},
{
    'question': 'What is the Strong Form of EMH, and how does it differ from the other forms?', 
    'answer': ['The Strong Form of EMH asserts that all information, both public and private (including insider information), is fully reflected in stock prices. This implies that even insiders with access to confidential company data cannot achieve abnormal returns, as prices have already adjusted to account for that information. The key difference between the strong form and the other forms of EMH is the inclusion of private information. While the weak form only considers historical data and the semi-strong form incorporates public data, the strong form suggests that no one, including corporate insiders, can exploit information to gain an advantage.', 'image: '], 
    'repeats': 1
},
{
    'question': 'How does the Random Walk Hypothesis relate to the Efficient Market Hypothesis?', 
    'answer': ['', 'image: The Random Walk Hypothesis suggests that stock prices evolve according to a random path, meaning that future price movements are unpredictable and independent of past price changes. This concept aligns with the EMH, particularly its weak form, by asserting that since prices already reflect all available information, new price movements will only result from the arrival of new, random, and unpredictable information. Thus, any attempt to use past price patterns or trends to predict future price movements is futile, as price changes follow a "random walk."'], 
    'repeats': 1
},
{
    'question': 'What are the implications of EMH on technical analysis?', 
    'answer': ['', 'image: According to the EMH, particularly in its weak and semi-strong forms, technical analysis is ineffective. Technical analysis relies on examining historical price data and volume patterns to predict future movements. However, EMH suggests that all past price data is already reflected in current prices, and new price movements are random. Therefore, trying to exploit historical patterns like trends, support, resistance levels, or moving averages will not consistently yield profits. Any success derived from technical analysis is more likely due to luck rather than skill.'], 
    'repeats': 1
},
{
    'question': 'Discuss the concept of event studies in the context of EMH.', 
    'answer': ['', 'image:  Event studies analyze how specific events, such as earnings reports, corporate mergers, or regulatory changes, affect stock prices. The goal is to determine if these events lead to abnormal returns—returns that deviate from what is expected based on a pricing model like the Capital Asset Pricing Model (CAPM). Under the EMH, particularly the semi-strong form, markets are expected to quickly incorporate new information into prices, leaving little room for investors to earn abnormal returns after the event has occurred. Researchers calculate the "normal return" (what the stock would have earned without the event) and compare it to the actual return. Any difference, called the "abnormal return," reflects the markets reaction to the event. The challenge in event studies is isolating the effect of the event itself from other market factors.'], 
    'repeats': 1
},
{
    'question': 'How does the EMH affect resource allocation in the economy?', 
    'answer': ['', 'image: Under the EMH, financial markets efficiently allocate resources by ensuring that securities are accurately priced based on all available information. When prices are correct, capital flows to the most productive uses, supporting economic growth and innovation. However, if markets are inefficient, securities may be mispriced, leading to a misallocation of resources. For example, overvalued firms may receive too much investment, while undervalued but more efficient firms may struggle to raise capital. This can result in economic inefficiencies, as resources are directed towards less productive sectors, ultimately hindering growth.'], 
    'repeats': 1
},
{
    'question': 'What is the "Small-Firm-in-January" Effect, and how does it challenge the EMH?', 
    'answer': ['', 'image: The "Small-Firm-in-January" Effect is a market anomaly where smaller firms consistently outperform larger firms, especially in the month of January. Studies show that small-cap stocks tend to generate higher average returns than large-cap stocks during this period, which contradicts the EMH’s assertion that markets are efficient and such predictable patterns should not exist. Even when risk adjustments are made using models like CAPM, small firms still exhibit higher returns. This raises questions about whether markets are truly efficient or whether this effect is due to higher risk premiums associated with smaller firms or liquidity constraints.'], 
    'repeats': 1
},
{
    'question': 'How does risk adjustment play a role in testing market anomalies under EMH?', 
    'answer': ['', 'image: When testing market anomalies, such as the Small-Firm Effect or momentum strategies, it is crucial to adjust returns for risk. Models like the Capital Asset Pricing Model (CAPM) are often used to determine whether excess returns are due to skill or simply compensation for additional risk. If, after adjusting for risk, the anomaly still shows significant excess returns, it might suggest a violation of EMH. However, if the anomaly disappears after proper risk adjustment, it may indicate that the additional returns were simply compensation for taking on higher risk, not an inefficiency in the market. Testing these anomalies requires careful use of risk models, and the accuracy of these tests depends on whether the chosen model correctly accounts for all relevant risk factors.'], 
    'repeats': 1 #Forelesning 7.5
},
{
    'question': '', 
    'answer': ['', 'image: '], 
    'repeats': 1
},



]

total_questions = len(flashcards)  # Total number of questions
answered_questions = 0  # Start with 0 answered

# Function to split text into multiple lines to fit within a maximum width
def split_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        # Check if adding the next word exceeds the max_width
        if font.size(current_line + word)[0] < max_width:
            current_line += word + " "
        else:
            lines.append(current_line)  # Store the current line and start a new one
            current_line = word + " "

        # Handle a word that is longer than the max_width
        while font.size(word)[0] >= max_width:  # If word is too long, break it
            current_line = word[:max_width // font.size(' ')[0]] + "-"
            word = word[max_width // font.size(' ')[0]:]
            lines.append(current_line)
            current_line = word
    
    lines.append(current_line)  # Append any remaining text
    return lines

# Function to display the counters on the screen
def show_counters():
    counter_text = f"Answered: {answered_questions} / {total_questions}"
    counter_surface = font.render(counter_text, True, BLACK)
    screen.blit(counter_surface, (WIDTH - 300, 20))  # Adjust the positioning slightly to fit

# Function to draw multiple lines of text on the screen
def draw_text_multiline(text, font, color, surface, x, y, max_width):
    lines = split_text(text, font, max_width)
    for i, line in enumerate(lines):
        text_obj = font.render(line, True, color)
        surface.blit(text_obj, (x, y + i * font.get_linesize()))  # Render each line on the screen

# Function to display the question on the screen
def show_question(card):
    screen.fill(GREEN)
    draw_text_multiline(card['question'], font, BLACK, screen, 50, 100, 1000)
    show_counters()  # Show the counters at the top
    pygame.display.flip()

# Function to display the answer, including both text and images
def show_answer(card, selected=None):
    screen.fill(GREEN)
    
    y_offset = 100  # Starting position for displaying text
    
    for item in card['answer']:
        if item.startswith('image:'):
            image_path = item.replace('image:', '').strip()
            
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (700, 450))  # Resize the image
                image_rect = image.get_rect(center=(WIDTH // 2, y_offset + 350))  # Adjust y_offset for placing the image
                screen.blit(image, image_rect)
                y_offset += 450  # Adjust y_offset after displaying the image
            else:
                draw_text_multiline(f"Image not found: {image_path}", font, BLACK, screen, 50, y_offset, 1000)
                y_offset += 50
        else:
            draw_text_multiline(item, font, BLACK, screen, 50, y_offset, 1000)
            y_offset += font.get_linesize() * len(split_text(item, font, 1000))  # Adjust y_offset after text
    
    # Display a confirmation of the selection
    if selected == 'cant':
        draw_text_multiline("You selected: Can't", font, RED, screen, 50, y_offset, 1000)
    elif selected == 'medium':
        draw_text_multiline("You selected: Medium", font, YELLOW, screen, 50, y_offset, 1000)
    elif selected == 'can':
        draw_text_multiline("You selected: Can", font, BLUE, screen, 50, y_offset, 1000)

    # Display buttons for "Can't", "Medium", "Can"
    pygame.draw.rect(screen, DARK_RED if selected == 'cant' else RED, [50, HEIGHT - 100, 200, 50])  # "Can't" button
    pygame.draw.rect(screen, DARK_YELLOW if selected == 'medium' else YELLOW, [300, HEIGHT - 100, 200, 50])  # "Medium" button
    pygame.draw.rect(screen, DARK_BLUE if selected == 'can' else BLUE, [550, HEIGHT - 100, 200, 50])  # "Can" button

    draw_text_multiline("Can't", font, WHITE, screen, 100, HEIGHT - 95, 200)  # "Can't" text
    draw_text_multiline("Medium", font, BLACK, screen, 350, HEIGHT - 95, 200)  # "Medium" text
    draw_text_multiline("Can", font, WHITE, screen, 600, HEIGHT - 95, 200)  # "Can" text

    show_counters()  # Show the counters at the top
    pygame.display.flip()

# Function to update the number of repeats based on user selection
def update_repeats(card, selection):
    if selection == 'cant':
        card['repeats'] = 2  # If user selects "Can't", show it 3 times next round
    elif selection == 'medium':
        card['repeats'] = 1  # If user selects "Medium", show it 2 times next round
    elif selection == 'can':
        card['repeats'] = 0  # If user selects "Can", show it 1 time next round

# Function to show the end menu
def show_end_menu():
    screen.fill(GREEN)
    draw_text_multiline("All questions completed!", font, BLACK, screen, 50, 200, 1000)
    draw_text_multiline("Press S to restart or Q to quit", font, BLACK, screen, 50, 300, 1000)
    pygame.display.flip()

# Function to restart the game, adjusting the frequency of questions based on user selections
def restart_game():
    global remaining_cards, current_card, showing_answer, selected, answered_questions
    remaining_cards = []  # Clear the list of remaining cards
    
    # Add each flashcard according to its repeat count
    for card in flashcards:
        remaining_cards.extend([card] * card['repeats'])
    
    random.shuffle(remaining_cards)  # Shuffle the flashcards
    current_card = remaining_cards.pop()
    showing_answer = False
    selected = None  # Reset selection for the new game
    answered_questions = 0  # Reset answered questions count
    show_question(current_card)

# Start by shuffling the questions and setting up a queue of flashcards
remaining_cards = random.sample(flashcards, len(flashcards))
current_card = remaining_cards.pop()
showing_answer = False  # Flag to track if the answer is being shown
selected = None  # Variable to keep track of which button is pressed

# Show the first question
show_question(current_card)

running = True
end_game = False  # Variable to control whether we are at the end of the game

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not end_game:  # Handle mouse click when the game is running
            mouse_x, mouse_y = event.pos  # Get the position of the mouse click
            
            if not showing_answer:  # If the answer is not being shown, show it on the first click
                show_answer(current_card)
                showing_answer = True  # Now showing the answer
            
            else:  # If the answer is being shown, only allow button clicks
                # Check if user clicks one of the answer buttons on the answer screen
                if 50 <= mouse_x <= 250 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'cant')  # User chose "Can't"
                    selected = 'cant'  # Track the selection
                elif 300 <= mouse_x <= 500 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'medium')  # User chose "Medium"
                    selected = 'medium'  # Track the selection
                elif 550 <= mouse_x <= 750 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'can')  # User chose "Can"
                    selected = 'can'  # Track the selection
                
                # Only move to the next question if a button was clicked
                if selected is not None:
                    answered_questions += 1  # Increment the answered question count
                    if len(remaining_cards) == 0:  # When all questions are used up
                        show_end_menu()  # Show end menu
                        end_game = True  # Set end of game flag
                    else:
                        current_card = remaining_cards.pop()
                        show_question(current_card)
                        showing_answer = False  # Reset for next round
                        selected = None  # Reset the selection for the new card
        
        if end_game:  # Handle end menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Press S to restart
                    restart_game()  # Restart the game
                    end_game = False  # Return to game
                    selected = None  # Reset the selection
                elif event.key == pygame.K_q:  # Press Q to quit
                    running = False  # Exit the game

# Quit pygame
pygame.quit()