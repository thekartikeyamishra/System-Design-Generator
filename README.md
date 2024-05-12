# System-Design-Generator
The System-Design-Generator is a Streamlit-powered web application designed to empower developers in the critical early stages of project planning. It streamlines the often-daunting task of choosing a software architecture by providing:

Interactive Visualization: Generate clear, informative diagrams for various software architectures, including microservices, monolithic, event-driven, layered, and even custom user-defined structures.

Pre-Defined Templates: Quickly explore common architectural patterns with pre-loaded templates, each accompanied by a visual representation to aid understanding.

Customizable Designs:  Tailor the architecture to your specific needs by defining custom components, relationships, and styles in a simple JSON format.

Learning Resources: Gain insights into each architecture through curated resources, ensuring you have the knowledge to make informed decisions.

Error Handling and Validation:  Receive immediate feedback on any errors in your custom architecture definitions, helping you avoid common pitfalls.

Whether you're a student learning the ropes, a freelancer assessing client projects, or a seasoned engineer seeking a visual reference, the System-Design-Generator simplifies the architecture selection process, saving you valuable time and effort.

Jumpstart your next project with the Project Idea Generator! This intuitive Streamlit app helps you visualize and understand various software architectures.

## Features

- **Interactive Diagrams:** Generate clear visuals for a wide range of architectures.
- **Pre-defined Templates:** Explore common architectures like microservices, monolithic, etc.
- **Custom Designs:** Create your own architecture diagrams with a simple JSON format.
- **Resource Links:** Access relevant tutorials and documentation for each architecture.
- **Error Handling:** Get feedback on invalid custom architecture definitions.

## How to Use
Enter your project idea in the text box.
Choose a pre-defined architecture or define your own.
Click "Generate Diagram" (if you defined your own).
Explore the interactive diagram and learn about the architecture.

## Defining Custom Architectures (JSON format)
{
    "name": "Custom Architecture",
    "nodes": [
        {"name": "Component A", "shape": "box", "color": "lightblue"},
        {"name": "Component B", "shape": "ellipse", "color": "orange"}
    ],
    "edges": [
        {"source": "Component A", "target": "Component B", "style": "solid"}
    ],
    "resources": [
        {
            "title": "Research the Specific Components in Your Design",
            "url": "[invalid URL removed]" 
        }
        // Add more resources here...
    ]
}

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

