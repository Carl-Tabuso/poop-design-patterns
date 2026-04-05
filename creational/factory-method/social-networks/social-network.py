from SocialNetworkPoster import SocialNetworkPoster
from FacebookPoster import FacebookPoster
from LinkedInPoster import LinkedInPoster

def post_content_on(social_network: SocialNetworkPoster):
    social_network.post(f"This is my first {social_network.get_platform_name()} post.")

if __name__ == "__main__":
    facebook = FacebookPoster('user@fb.com', '12345678')
    linkedin = LinkedInPoster('user@ln.com', '87654321')

    post_content_on(facebook)
    print("\n")
    post_content_on(linkedin)