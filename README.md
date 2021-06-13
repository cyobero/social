# social
A social media site a la MySpace. 

## To-Do
==================================================================

### Features
- ~~Users can add/change their profile pictures so others know who they are. (2.5/5) 
	- Create template for profile pic.~~
- ~~Users can add friends to their friends list so they can see each other's content.~~ (3.5/5)
- ~~Users can create and edit their profile page so they can share information and content with others. (3.5/5)~~
- ~~Users can write blurbs (texts that are larger than tweets but smaller than blogs) so
	they can share their thoughts, opinions, and feelings.~~
- Users can add a "top 8" friends to their profile page.
- Users can sort their top 8 by dragging and dropping (see jQuery 'sortable').
- Users can add extra fields to their bio.
- Users can make their profiles private (only their friends can view).
- Users can send other users messages.


- Style navbar (2.5)
- Style comment form. (2.5)
- Style profile card.
- Only show the `k` latest blurbs for each profile.


# Models
## User Profile
==================================================================
### Fields (all fields in addition to django's `User` model are optional):
	- profile picture
	- first name
	- last name
	- birthdate
	- gender
	- occupation
	- education
	- hobbies

## Blurb
