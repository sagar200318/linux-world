import streamlit as st

# Sample data for rooms
rooms = [
    {
        "id": 1,
        "location": "Downtown",
        "price": 5000,
        "size": "Single",
        "amenities": ["WiFi", "Air Conditioner", "Bed"]
    },
    {
        "id": 2,
        "location": "Suburbs",
        "price": 3000,
        "size": "Shared",
        "amenities": ["WiFi", "Kitchen"]
    },
    {
        "id": 3,
        "location": "City Center",
        "price": 4500,
        "size": "Single",
        "amenities": ["WiFi", "Gym", "Air Conditioner"]
    },
    {
        "id": 4,
        "location": "Suburbs",
        "price": 2500,
        "size": "Shared",
        "amenities": ["WiFi"]
    },
    # Add more room data as needed
]

st.title("Student Room Rent Finder")

st.sidebar.header("Filter Options")

# User inputs
location_filter = st.sidebar.selectbox("Select Location", options=["Any", "Downtown", "Suburbs", "City Center"])
price_min = st.sidebar.slider("Minimum Price", min_value=1000, max_value=10000, value=2000, step=500)
price_max = st.sidebar.slider("Maximum Price", min_value=1000, max_value=20000, value=6000, step=500)
size_filter = st.sidebar.selectbox("Room Size", options=["Any", "Single", "Shared"])
amenities_filter = st.sidebar.multiselect("Amenities", options=["WiFi", "Air Conditioner", "Bed", "Kitchen", "Gym"])

# Filter rooms based on user input
filtered_rooms = []

for room in rooms:
    if location_filter != "Any" and room["location"] != location_filter:
        continue
    if not (price_min <= room["price"] <= price_max):
        continue
    if size_filter != "Any" and room["size"] != size_filter:
        continue
    if amenities_filter:
        if not all(amenity in room["amenities"] for amenity in amenities_filter):
            continue
    filtered_rooms.append(room)

st.write(f"Found {len(filtered_rooms)} matching rooms:")

# Display filtered rooms
for room in filtered_rooms:
    st.subheader(f"Room ID: {room['id']}")
    st.write(f"**Location:** {room['location']}")
    st.write(f"**Price:** ${room['price']} per month")
    st.write(f"**Size:** {room['size']}")
    st.write(f"**Amenities:** {', '.join(room['amenities'])}")
    st.markdown("---")