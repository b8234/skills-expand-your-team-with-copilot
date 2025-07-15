# Example: Well-Structured Issue Using Templates

This is an example of the kind of clear, actionable issue that teachers can create using the new issue templates. Compare this to the previous unclear requests.

## Before (unclear request):
```
Title: Fix the colors
Body: The website is blue, but our school colors are white and lime green. Please fix this.
```

## After (using Content Update template):
```
Title: [CONTENT] Update school colors from blue to lime green and white

**Content Update Title:** Update school colors from blue to lime green and white

**Type of Content:** School Information (name, colors, etc.)

**Current Content:** The website currently uses blue as the primary color throughout the interface

**New Content:** 
- Primary color: Lime green (#32CD32)
- Secondary color: White (#FFFFFF)  
- Accent color: Dark green (#006400)

**Location in System:** Overall Site Theme

**Specific Location Details:** This affects the header background, button colors, link colors, and any branded elements throughout the site

**Reason for Change:** School rebranding - our official school colors are lime green and white, and the website should reflect our school identity

**Implementation Hints:** Look for CSS variables or theme files that control the color scheme. May need to update both the main stylesheet and any component-specific styling.

**Acceptance Criteria:**
- [x] Old blue colors are completely replaced with lime green and white color scheme
- [x] Colors appear correctly in all specified locations  
- [x] No spelling or formatting errors in new content
- [x] Colors are consistent with overall system style/tone

**Additional Context:** Our school mascot is the "Green Dragons" and our sports teams use lime green jerseys. The new colors should feel energetic and school-spirited. Please ensure sufficient contrast for accessibility.
```

## Key Improvements:

1. **Specific Title**: Clearly identifies the type and scope of change
2. **Complete Information**: All necessary details provided upfront
3. **Clear Acceptance Criteria**: Measurable criteria for completion  
4. **Implementation Hints**: Guidance for the developer
5. **Context**: Background information that helps with implementation decisions
6. **Structured Format**: Easy for Copilot coding agent to parse and understand

This level of detail allows the Copilot coding agent to begin work immediately without needing to ask follow-up questions or make assumptions about requirements.