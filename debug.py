from send_email import extract_contacts, extract_summary, create_template, create_plot
import os
import fire

if __name__ == '__main__':
  # Export to Fire
  fire.Fire(extract_contacts)
  # fire.Fire(extract_summary)
  # fire.Fire(create_template)
  fire.Fire(create_plot)