# pets-api

## Overview

OnlyPets is a Pet social media site, similar to instagram, where a User can signup and add their Pet's profile to the site. A User can have multiple Pet profiles allowing them to like, comment (post-mvp), add posts, and delete their account.

## Prerequisites

```
Python 3
pip (Python package manager)
Virtual environment (recommended for Python package management)

```

### Base URL

```javascript
urlpatterns = [
   "admin/"
   "api/"
]
```

### Endpoints

These endpoints are out of the box Django providing full CRUD for each endpoint listed

```
"pets/"
"posts/"
"comments/"
"likes/"
"following/"
```

### Additional Endpoints

```javascript
urlpatterns = [
  POST "users/register/", registers a user
  POST "users/login/", adds a token to logged in User
  GET "users/verify/", verifies the User is authenticated
  GET  "user/pets/", gets all pets associated with a User
  GET "pet/<int:pet_id>/posts/", gets all posts from a specific Pet under User
  DELETE "users/delete/<int:user_id>/", Deletes a User and all associated Pets && Posts
]
```

## Models

### Pet Model:

```javascript
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('not specified', 'not specified'),
)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.URLField(max_length=600)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=True)
    bio = models.CharField(max_length=600, blank=True)

        def __str__(self):
        return f'{self.name} - {self.breed}'
```

### Post Model:

```javascript
class Post(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    post_image = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pet.name} - {self.content}'

```

### Like Model:

```javascript
class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Comment Model:

```javascript
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pet}- {self.comment}'

```

### Following Model:

```javascript
class Following(models.Model):
    follower = models.ForeignKey(Pet, related_name='following', on_delete=models.CASCADE)
    followed_pet = models.ForeignKey(Pet, related_name='followers', on_delete=models.CASCADE, null=True, blank=True)

```

## Contact

For any questions or concerns, please [open an issue](https://github.com/SEI-NightHawks/pets-api/issues) in this repository.
