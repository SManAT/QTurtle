import re
from typing import Dict


class cssTool:

    def update_css_styles(self, css_string: str, styles_dict: Dict[str, str]) -> str:
        """
        Updates CSS string by replacing existing styles or adding new ones from a dictionary.

        Args:
            css_string (str): The original CSS string
            styles_dict (dict): Dictionary with CSS properties as keys and values as values
                              Example: {'font-size': '11pt', 'color': 'blue'}

        Returns:
            str: Updated CSS string with modified/added styles
        """
        if not css_string.strip():
            # If CSS string is empty, create new styles from dict
            return "; ".join([f"{prop}: {value}" for prop, value in styles_dict.items()])

        # Remove trailing semicolon and split by semicolon
        css_string = css_string.rstrip(";")
        css_parts = [part.strip() for part in css_string.split(";") if part.strip()]

        # Parse existing CSS into a dictionary
        existing_styles = {}
        for part in css_parts:
            if ":" in part:
                prop, value = part.split(":", 1)
                existing_styles[prop.strip()] = value.strip()

        # Update with new styles (this will replace existing ones or add new ones)
        existing_styles.update(styles_dict)

        # Rebuild CSS string
        updated_css = "; ".join([f"{prop}: {value}" for prop, value in existing_styles.items()])

        return updated_css

    # Alternative method using regex (more robust for complex CSS)
    def update_css_styles_regex(self, css_string: str, styles_dict: Dict[str, str]) -> str:
        """
        Updates CSS string using regex for more robust parsing.

        Args:
            css_string (str): The original CSS string
            styles_dict (dict): Dictionary with CSS properties and values

        Returns:
            str: Updated CSS string
        """
        result_css = css_string.strip()

        for property_name, property_value in styles_dict.items():
            # Escape property name for regex
            escaped_prop = re.escape(property_name)

            # Pattern to match the property (case-insensitive)
            pattern = rf"\b{escaped_prop}\s*:\s*[^;]*"
            replacement = f"{property_name}: {property_value}"

            # Check if property exists and replace it
            if re.search(pattern, result_css, re.IGNORECASE):
                result_css = re.sub(pattern, replacement, result_css, flags=re.IGNORECASE)
            else:
                # Add new property
                if result_css and not result_css.endswith(";"):
                    result_css += "; "
                elif result_css:
                    result_css += " "
                result_css += replacement

        return result_css
