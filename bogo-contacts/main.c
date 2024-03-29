#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int displayMainMenu()
{
	int choice;
	printf("\nWelcome to BOGO Contacts\n");
	printf("1. Bogo will add a contact\n");
	printf("2. Bogo will remove a contact\n");
	printf("3. Bogo will edit a contact\n");
	printf("4. Bogo will display a contact\n");
	printf("0. Bogo will kick you out\n");
	scanf("%d", &choice);
	return choice;
}

struct Contact
{
	char name[50];
	char phone[50];
	char email[50];
};

void addContact()
{
	struct Contact contact;
	
	printf("Bogo needs a name: ");
	scanf(" %[^\n]", contact.name);

	printf("Bogo needs a phone: ");
	scanf(" %[^\n]", contact.phone);

	printf("Bogo needs a email: ");
	scanf(" %[^\n]", contact.email);

	// opening file
	FILE *aFile;
	aFile = fopen("contact.txt", "a");
	// error handling
	if (aFile == NULL)
	{
		perror("Error writing file\n");
		return;
	}
	// writing to file and closing
	fprintf(aFile, "%s\n%s\n%s\n---\n", contact.name, contact.phone, contact.email);
	fclose(aFile);

	printf("Bogo has added a contact\n");
}

void removeContact()
{
	FILE *rFile, *aFile;
	char line[50];
	char searchName[50];
	char temp_file[] = "temp.txt";
	printf("Bogo needs the contact name to remove: ");
	scanf(" %[^\n]", searchName);

	rFile = fopen("contact.txt", "r");
	aFile = fopen(temp_file, "a");
	// error handling
	if (rFile == NULL)
	{
		perror("Error reading file\n");
		return;
	}
	if (aFile == NULL)
	{
		perror("Error writing file\n");
		return;
	}

	int skip_count = 0;

	while (fgets(line, sizeof(line), rFile))
	{
		char *match = strstr(line, searchName);

		// configuring skip count
		if (skip_count == 0 && match != NULL)
		{
			skip_count = 1;
		}

		if (skip_count > 0 && skip_count < 5) 
		{
			skip_count++;
		}
		else
		{
			fputs(line, aFile);
		}
		
	}

	// close files
	fclose(rFile);
	fclose(aFile);
	// replace temp with contact
	if (remove("contact.txt"))
	{
		perror("Error deleting original file\n");
		return;
	}

	if (rename(temp_file, "contact.txt"))
	{
		perror("Error renaming temp file\n");
		return;
	}

	printf("Bogo has removed a contact\n");
}

void editContact()
{
	// getting info
	printf("1. Edit name\n2. Edit phone\n3. Edit email\n");
	int choice;
	char infoToEdit[50];
	scanf("%d", &choice);
	if (choice == 1) {snprintf(infoToEdit, sizeof(infoToEdit), "name");}
	else if (choice == 2) {snprintf(infoToEdit, sizeof(infoToEdit), "phone");}
	else if (choice == 3) {snprintf(infoToEdit, sizeof(infoToEdit), "email");}

	char oldInfo[50];
	char newInfo[50];

	printf("Give Bogo the old %s: ", infoToEdit);
	scanf(" %[^\n]", oldInfo);
	printf("Give Bogo the new %s: ", infoToEdit);
	scanf(" %[^\n]", newInfo);

	// file read write prep
	FILE *rFile, *aFile;

	char line[50];
	char temp_file[] = "temp.txt";
	char doEdit = 1; // edit only the first occurance (in case of name edit)

	rFile = fopen("contact.txt", "r");
	aFile = fopen(temp_file, "a");
	// error handling
	if (rFile == NULL)
	{
		perror("Error reading file\n");
		return;
	}
	if (aFile == NULL)
	{
		perror("Error writing file\n");
		return;
	}

	while (fgets(line, sizeof(line), rFile))
	{
		char *match = strstr(line, oldInfo);

		// configuring skip count
		if (match != NULL && doEdit)
		{
			fprintf(aFile, "%s\n", newInfo);
			doEdit = 0;
		}
		else
		{
			fputs(line, aFile);
		}
	}

	// close files
	fclose(rFile);
	fclose(aFile);
	// replace temp with contact
	if (remove("contact.txt"))
	{
		perror("Error deleting original file\n");
		return;
	}

	if (rename(temp_file, "contact.txt"))
	{
		perror("Error renaming temp file\n");
		return;
	}
	
	printf("Bogo has edited a contact\n");
}

void displayContact()
{
	FILE *rFile;
	rFile = fopen("contact.txt", "r");
	char searchName[50];
	printf("Bogo needs the contact name: ");
	scanf(" %[^\n]", searchName);

	char line[50];
	int count = 0;

	while (fgets(line, sizeof(line), rFile))
	{
		char *match = strstr(line, searchName);
		
		// configuring skip count
		if (count == 0 && match != NULL)
		{
			count = 1;
		}

		if (count > 0 && count < 5) 
		{
			if (count == 1) {printf("Name: %s", line);}
			else if (count == 2) {printf("Phone: %s", line);}
			else if (count == 3) {printf("Email: %s", line);}
			count++;
		}
	}
	fclose(rFile);
}

int main()
{
	while(1)
	{
		int choice = displayMainMenu();

		if (choice == 1)
		{
			addContact();
		}
		else if (choice == 2)
		{
			removeContact();
		}
		else if (choice == 3)
		{
			editContact();
		}
		else if (choice == 4)
		{
			displayContact();
		}
		else if (choice == 0)
		{
			break;
		}
		else
		{
			printf("CAUTION: DON'T MAKE BOGO ANGRY.\n");
		}
	}

	return 0;
}