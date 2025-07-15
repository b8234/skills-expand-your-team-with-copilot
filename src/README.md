# Mergington High School Activities

A comprehensive web application that allows students to browse, filter, and sign up for extracurricular activities, with a management interface for teachers and administrators.

## Features

### Student Features
- **Browse Activities**: View all 13+ available extracurricular activities including Chess Club, Programming Class, Sports Teams, Art Club, Drama Club, Robotics Workshop, and more
- **Advanced Filtering**: Filter activities by:
  - Category (Sports, Arts, Academic, Community, Technology)
  - Day of the week (Monday through Sunday)
  - Time slot (Before School, After School, Weekend)
- **Search Functionality**: Search activities by name or description
- **Activity Details**: View comprehensive information including:
  - Detailed descriptions and schedules
  - Maximum participant limits
  - Current enrollment status
  - Meeting times and days
- **Easy Registration**: Sign up for activities through an intuitive modal interface

### Teacher/Administrator Features
- **Secure Authentication**: Teacher login system with password-protected access
- **Activity Management**: Manage extracurricular activities and enrollments
- **User Management**: View and manage student registrations

### Technical Features
- **Modern Web Interface**: Responsive design with interactive modals and real-time filtering
- **RESTful API**: FastAPI backend with comprehensive endpoints for activities and authentication
- **Database Integration**: MongoDB integration for persistent data storage
- **Security**: Password hashing with Argon2 for secure teacher authentication
- **Real-time Updates**: Live filtering and search without page reloads

## Activity Catalog

The system includes a diverse range of activities:
- **Academic**: Chess Club, Programming Class, Math Club, Debate Team, Science Olympiad
- **Sports**: Soccer Team, Basketball Team, Morning Fitness
- **Arts**: Art Club, Drama Club, Manga Maniacs
- **Technology**: Weekend Robotics Workshop
- **Competition**: Sunday Chess Tournament, Science Olympiad

Each activity includes detailed scheduling information, participant limits, and current enrollment data.

## Development Guide

For detailed setup and development instructions, please refer to our [Development Guide](../docs/how-to-develop.md).
