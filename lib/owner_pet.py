class Pet:
    # Class variable for valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    # Class variable to store all instances of the Pet class
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        # Initialize pet attributes
        self.name = name
        self.pet_type = pet_type
        
        # Validate pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        
        # Assign the owner if provided
        self.owner = owner
        
        # If owner is provided, add this pet to the owner's pets list
        if owner:
            owner.add_pet(self)  # Add the pet to the owner's pets

        # Add the current pet instance to the all list
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []  # Initialize a list to store this owner's pets

    # Method to get all pets of this owner
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

   
    def add_pet(self, pet):
       
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class")
        
        # Assign the pet's owner to this owner
        pet.owner = self
        self.pets_list.append(pet)  

   
    def get_sorted_pets(self):
        # Sort pets by their names
        return sorted(self.pets(), key=lambda pet: pet.name)
