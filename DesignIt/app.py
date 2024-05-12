import streamlit as st
import json
from graphviz import Digraph
import os

# Load architecture templates from JSON files
def load_template(filename):
    with open(f"templates/{filename}") as f:
        return json.load(f)

# Generate flowchart based on template
def generate_flowchart(template_data):
    dot = Digraph(comment=template_data["name"])
    for node in template_data["nodes"]:
        dot.node(node["name"], shape=node.get("shape", "box"), color=node.get("color", "black"))
    for edge in template_data["edges"]:
        dot.edge(edge["source"], edge["target"], style=edge.get("style", "solid"))
    return dot

st.title("System Design Generator")
project_idea = st.text_input("Enter your project idea:")

if project_idea:
    arch_type = st.selectbox("Architecture Type:", ["Pre-defined", "User-defined"])

    if arch_type == "Pre-defined":
        templates = [f.replace(".json", "") for f in os.listdir("templates") if f.endswith(".json")]
        selected_design = st.selectbox("Choose a system design approach:", templates)
        template_data = load_template(f"{selected_design}.json")

        flowchart = generate_flowchart(template_data)
        st.subheader(f"{template_data['name']} Architecture")
        st.graphviz_chart(flowchart)

        if "image" in template_data:
            st.image(os.path.join(os.getcwd(), "assets", template_data['image']))

        # Resources section
        st.subheader("Resources")
        if "resources" in template_data:
            for resource in template_data["resources"]:
                st.write(f"- [{resource['title']}]({resource['url']})")
        else:
            st.write("No resources found for this architecture.")

    elif arch_type == "User-defined":
        st.subheader("Define Your Architecture")
        user_defined_arch = st.text_area("Enter your architecture in JSON format:", height=300)

        if st.button("Generate Diagram"):
            try:
                template_data = json.loads(user_defined_arch)

                # Input validation 
                required_keys = ["name", "nodes", "edges"]
                for key in required_keys:
                    if key not in template_data:
                        raise ValueError(f"Missing required key: '{key}'")

                for node in template_data["nodes"]:
                    if "name" not in node or "shape" not in node:
                        raise ValueError("Invalid node format. Each node must have a 'name' and a 'shape'.")

                for edge in template_data["edges"]:
                    if "source" not in edge or "target" not in edge:
                        raise ValueError("Invalid edge format. Each edge must have a 'source' and a 'target'.")

                flowchart = generate_flowchart(template_data)
                st.graphviz_chart(flowchart)

                # Display user-provided resources
                if "resources" in template_data:
                    st.subheader("Resources")
                    for resource in template_data["resources"]:
                        st.write(f"- [{resource['title']}]({resource['url']})")


            except json.JSONDecodeError:
                st.error("Invalid JSON format.")
            except ValueError as e:
                st.error(str(e))
