# Displaying NYCT station accessibility and elevator

Column: https://new.mta.info/developers/display-elevators-NYCT
Processed: No
created on: January 23, 2024 7:26 AM

![social_image.jpg](Displaying%20NYCT%20station%20accessibility%20and%20elevator%206ecc683fdc2441d0ba6004409c2f9cf1/social_image.jpg)

We want to make sure our partners the best information about which stations are accessible. Here’s how to programmatically find information about station accessibility to display in your digital products.

## Is a station ADA accessible or not

### The NYCT Station Location file shows station accessibility

Not every station that has an elevator is ADA accessible. We publish a canonical list of subway station information in a .csv format that you can use to display station accessibility. This is updated frequently and lives in a canonical location in the New York State open data portal that you can programmatically check.

Stations are broken down to their unique GTFS Stop ID level. For reference to Station Complex accessibility, you can see the “[Station Complexes](https://data.ny.gov/Transportation/MTA-Subway-Station-Complexes/4ta5-wz5s)” file at the same website.

[MTA subway stations data set](https://data.ny.gov/Transportation/MTA-Subway-Stations/39hk-dx4f)

### Reading the file

Look at the **ADA** column.

- **0** means it’s not accessible,
- **1** means it is fully accessible, and
- **2** means it is partially accessible. Partially accessible stations are usually accessible in one direction.

If a station is partially accessible, a description of that accessibility is in the **ADA Direction Notes** column. For example, 49 St on the has an **ADA** value of 2 and **ADA Direction Notes** value of Uptown & Queens. This means that the station is accessible in the Uptown & Queens direction only.

## What elevators & escalators exist and are they in or out of service

The most helpful thing for riders is to show in real-time which elevators and escalators are in service at each station. We provide a live data feed you can use for this.

1. Create an account at [api.mta.info](https://api.mta.info/).

2. Go to "Elevator & Escalator"

3. There are two feeds:

1. Elevator and Escalator Equipment

2. Elevator and Escalator Current Outages

4. **Elevator and Escalator Equipment** tells you which elevators and escalators exist as well as important information about them like which station they are in, their location inside the station, lines they serve, and travel alternatives when they are out of service.

5. **Elevator and Escalator Current Outages** will tell you which elevators and escalators are out of service, the reason, and their estimated return to service.

6. You can use the equipment ID number **<equipmentno>** to connect the two sets of data.

## Tips for displaying elevator information

### How we display information

We try to show as much information as possible. You can see how we do it at our elevator & escalator lookup tool. We are in the middle of redesigning this, so it might change in the future.

[Check Elevator & Escalator status](https://new.mta.info/elevator-escalator-status)

### Tips for displaying yourself

You may want to show less information than we do, but here are a few things we've learned about what riders like to see.

- Elevators don’t have short names. We created the Short Description field **<shortdescription>** which is our best attempt at giving them names that are easy to display but also helpful to determine which elevator is which.
- Riders don’t just want to know if an elevator is out of service. They want to be able to verify that elevators are *in* service as well. This is especially true for riders who use wheelchairs. You may want to show all elevators.
- Riders really care about expected return to service date as well as travel alternatives. This information is in the **<alternativeeroute>** field.
- Not every elevator is part of an accessible pathway through a station. For example, at Clark St the elevators go to mezzanine but there is no step-free path to get from the mezzanine to the platform. We indicate if an elevator is part of an accessible pathway via the **<ADA>** field and recommend you show that to users.