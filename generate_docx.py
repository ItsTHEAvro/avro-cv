import zipfile
import os

doc_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    <!-- Header / Sender Info -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:b/>
          <w:sz w:val="32"/>
          <w:color w:val="1F497D"/>
        </w:rPr>
        <w:t>Jyotirmoy Avro</w:t>
      </w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:spacing w:after="200" w:line="240" w:lineRule="auto"/>
        <w:pBdr>
          <w:bottom w:val="single" w:sz="6" w:space="4" w:color="1F497D"/>
        </w:pBdr>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="20"/>
          <w:color w:val="595959"/>
        </w:rPr>
        <w:t>Dhaka, Bangladesh  |  (+880) 1735-342669  |  jyotirmoy.avro@gmail.com  |  linkedin.com/in/jyotirmoy-avro</w:t>
      </w:r>
    </w:p>

    <!-- Date -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="160" w:line="260" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>October 15, 2026</w:t>
      </w:r>
    </w:p>

    <!-- Recipient Info -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Mohammad Tawrit</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Chief Executive Officer (CEO)</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Bangladesh Research and Education Network (BdREN)</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="200" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Email: ceo@bdren.net.bd</w:t>
      </w:r>
    </w:p>

    <!-- Subject -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="180" w:line="260" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Subject: Application for Internship Position in Artificial Intelligence (AI)</w:t>
      </w:r>
    </w:p>

    <!-- Salutation -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="140" w:line="260" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Dear Sir,</w:t>
      </w:r>
    </w:p>

    <!-- Body Paragraph 1 -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="140" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>I am writing to express my strong interest in the Artificial Intelligence (AI) Internship opportunity at the Bangladesh Research and Education Network (BdREN). I am currently pursuing my MSc in Information and Communication Technology (ICT) at the Institute of Information and Communication Technology (IICT), Bangladesh University of Engineering and Technology (BUET), having completed my BSc in Computer Science and Engineering from Patuakhali Science and Technology University (PSTU). With a background in applied machine learning research, explainable AI (XAI), and practical AI automation, I am excited about the prospect of contributing to BdREN's mission while learning directly from your specialized engineers.</w:t>
      </w:r>
    </w:p>

    <!-- Body Paragraph 2 -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="140" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>My technical foundation aligns closely with the practical challenges addressed by BdREN in managing secure, high-throughput network infrastructure. For my undergraduate thesis, I developed a two-stage hierarchical ML-based Network Intrusion Detection System (NIDS) evaluated on modern traffic (CICIIoT2025). This work integrated model interpretability using SHAP and addressed critical real-world evaluation hurdles, including mitigating data leakage across temporal traffic splits. The resulting paper has been accepted for publication at COMPAS 2026 (University of Dhaka). This experience gave me solid hands-on expertise in feature engineering, model optimization, edge inference considerations, and rigorous performance validation.</w:t>
      </w:r>
    </w:p>

    <!-- Body Paragraph 3 -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="140" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Beyond classical machine learning, I actively work with modern LLMs, OpenAI API workflows, prompt engineering, and automated agent pipelines using n8n and Python. Additionally, having solved over 1,000 algorithmic problems across platforms, cleared all technical phases of Brain Station 23's Star Coder 2025, and secured 10th place at both the BUET CTF 2026 and BUP CTF 2025 national onsite finals, I bring disciplined problem-solving capabilities, strong coding standards, and a firm grasp of network systems and cybersecurity.</w:t>
      </w:r>
    </w:p>

    <!-- Body Paragraph 4 -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="160" w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>BdREN's position as the technological backbone connecting Bangladesh's higher education and research institutes presents an exceptional environment to apply data-driven intelligence to real-world infrastructure. I am eager to dedicate my technical skills, collaborative drive, and research curiosity to your AI initiatives. I welcome the opportunity to discuss how my academic background and project experience can add value to your ongoing and upcoming projects.</w:t>
      </w:r>
    </w:p>

    <!-- Sign-off -->
    <w:p>
      <w:pPr>
        <w:spacing w:after="120" w:line="260" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Thank you very much for your time and consideration.</w:t>
      </w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:spacing w:after="80" w:line="260" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Sincerely,</w:t>
      </w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:b/>
          <w:sz w:val="22"/>
        </w:rPr>
        <w:t>Jyotirmoy Avro</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="20"/>
          <w:color w:val="595959"/>
        </w:rPr>
        <w:t>MSc Student in ICT, IICT, BUET</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="20"/>
          <w:color w:val="595959"/>
        </w:rPr>
        <w:t>BSc in Computer Science and Engineering, PSTU</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:spacing w:after="40" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
          <w:sz w:val="20"/>
          <w:color w:val="595959"/>
        </w:rPr>
        <w:t>Phone: (+880) 1735-342669  |  Email: jyotirmoy.avro@gmail.com</w:t>
      </w:r>
    </w:p>

    <!-- Page setup: Standard Letter/A4 margins (1 inch = 1440 twips) -->
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""

content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""

rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

document_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""

styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
        <w:sz w:val="22"/>
        <w:lang w:val="en-US"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
  </w:style>
</w:styles>
"""

output_path = r"c:\Users\avro18\Downloads\cv-resume-tex\AI_Internship_Application_Jyotirmoy_Avro.docx"

with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
    docx.writestr("[Content_Types].xml", content_types)
    docx.writestr("_rels/.rels", rels)
    docx.writestr("word/_rels/document.xml.rels", document_rels)
    docx.writestr("word/styles.xml", styles_xml)
    docx.writestr("word/document.xml", doc_xml)

print(f"Generated successfully: {output_path}")
