-- SQLite 

-- Table utilisateur
-- CREATE TABLE users (
--     id INTEGER PRIMARY KEY,
--     username TEXT UNIQUE NOT NULL,
--     master_password TEXT NOT NULL
-- );

-- Table des mots de passe
-- CREATE TABLE passwords (
--     id INTEGER PRIMARY KEY,
--     user_id INTEGER,
--     titre TEXT NOT NULL,
--     username TEXT,
--     password TEXT NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- );


-- Insertion des utilisateurs généré grâce à Claude
INSERT INTO users (username, master_password) VALUES 
('alice_martin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/0mEirlHc6xlDBUux2'),
('bob_dupont', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPDw0mGgO'),
('claire_bernard', '$2b$12$8k1lde/.k8uFEd1J9zYls.hJty8bdI5ahkQEJ86M4y4rHmA2G4.x6');

-- Insertion des mots de passe pour Alice (user_id = 1)
INSERT INTO passwords (user_id, titre, username, password) VALUES 
(1, 'Gmail Personnel', 'alice.martin@gmail.com', 'Pr0t3ct3d_M@il2024!'),
(1, 'Compte Bancaire BNP', 'alice_martin', 'B@nk_S3cur3_789'),
(1, 'LinkedIn', 'alice.martin.dev', 'Link3d_Pr0f1l3#2024'),
(1, 'Netflix', 'alice.martin@gmail.com', 'N3tfl1x_W@tch2024'),
(1, 'Amazon', 'alice.martin@gmail.com', 'Am@z0n_Sh0pp1ng!');

-- Insertion des mots de passe pour Bob (user_id = 2)
INSERT INTO passwords (user_id, titre, username, password) VALUES 
(2, 'Facebook', 'bob.dupont75', 'F@c3b00k_S0c1@l2024'),
(2, 'Spotify', 'bob_music_lover', 'Sp0t1fy_Mus1c#789'),
(2, 'Gmail Professionnel', 'bob.dupont@entreprise.fr', 'Pr0_M@il_B0b2024!'),
(2, 'Steam Gaming', 'BobGamer75', 'St3@m_G@m3r_2024!'),
(2, 'Dropbox', 'bob.dupont@gmail.com', 'Dr0pb0x_Cl0ud#456');

-- Insertion des mots de passe pour Claire (user_id = 3)
INSERT INTO passwords (user_id, titre, username, password) VALUES 
(3, 'Instagram', 'claire_photos', 'Inst@_Ph0t0s2024!'),
(3, 'Compte Crédit Agricole', 'claire.bernard', 'C@_B@nk_Cl@1re789'),
(3, 'Adobe Creative Suite', 'claire.bernard@designer.com', '@d0be_Cr3@t1v3#2024'),
(3, 'GitHub', 'claire-dev', 'G1tHub_C0d3_2024!'),
(3, 'Discord', 'ClaireDev#1234', 'D1sc0rd_Ch@t_789'),
(3, 'Notion', 'claire.bernard@gmail.com', 'N0t1on_0rg@n1z3!');




INSERT INTO users (username, master_password) VALUES 
('admin', 'admin');

INSERT INTO passwords (user_id, titre, username, password) VALUES 
(4, 'Instagram', 'admin', 'Si je suis ici je suis content');




SELECT id
FROM users
WHERE EXISTS
(SELECT id FROM users WHERE username='admin' AND master_password='admin');